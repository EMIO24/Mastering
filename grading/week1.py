"""Behaviour checks for Week 1. This module has no third-party dependencies."""
import copy
import csv
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def equal(actual, expected):
    require(actual == expected, f'Expected {expected!r}; received {actual!r}')


def raises(types, operation):
    try:
        operation()
    except types:
        return
    raise AssertionError(f'Expected {types}; the call returned normally')


def products():
    return [
        {'id': 1, 'name': 'Pen', 'price': 200, 'stock': 10},
        {'id': 2, 'name': 'Notebook', 'price': 500, 'stock': 3},
        {'id': 3, 'name': 'Bag', 'price': 4000, 'stock': 0},
    ]


def bad_records():
    valid = products()[0]
    invalid = [{}, None, 'inventory', [None], [{}], [valid, valid.copy()]]
    for field in ('id', 'name', 'price', 'stock'):
        missing = valid.copy()
        del missing[field]
        invalid.append([missing])
    for field in ('id', 'price', 'stock'):
        for value in (-1, True, False, 1.5, '5', None):
            record = valid.copy()
            record[field] = value
            invalid.append([record])
    for value in ('', '   ', 123, None):
        invalid.append([dict(valid, name=value)])
    invalid.append([dict(valid, id=0)])
    return invalid


def check(name, module, work):
    """Each named criterion runs against fresh data in a temporary directory."""
    p = products()
    if name == 'stock_zero':
        equal(module.stock_label(0), 'out')
    elif name == 'stock_low':
        for stock in range(1, 6):
            equal(module.stock_label(stock), 'low')
    elif name == 'stock_available':
        for stock in (6, 12, 1000):
            equal(module.stock_label(stock), 'available')
    elif name == 'inventory_total':
        equal(module.inventory_value(p), 3500)
        equal(module.inventory_value([dict(p[0], price=7, stock=9)]), 63)
    elif name == 'inventory_empty':
        equal(module.inventory_value([]), 0)
    elif name == 'low_stock':
        equal(module.low_stock_names(p, 3), ['Notebook', 'Bag'])
        equal(module.low_stock_names(p, 0), ['Bag'])
        equal(module.low_stock_names(p, 10), ['Pen', 'Notebook', 'Bag'])
        equal(module.low_stock_names(p, -1), [])
    elif name == 'low_empty':
        equal(module.low_stock_names([], 3), [])
    elif name in ('find_match', 'lookup'):
        before = copy.deepcopy(p)
        for item in p:
            equal(module.find_product(p, item['id']), item)
        if name == 'lookup':
            equal(module.find_product(p, 99), None)
            equal(module.find_product([], 1), None)
        equal(p, before)
    elif name == 'find_missing':
        equal(module.find_product(p, 99), None)
        equal(module.find_product([], 1), None)
    elif name == 'find_unchanged':
        before = copy.deepcopy(p)
        module.find_product(p, 2)
        module.find_product(p, 99)
        equal(p, before)
    elif name == 'input_retry':
        # The message wording is reviewed manually; no fragile string matching.
        with patch('builtins.input', side_effect=['three', '2.5', '0', '-2', ' 3 ']) as prompt:
            result = module.read_positive_integer('Quantity: ')
            equal(result, 3)
            require(type(result) is int, 'Return an integer, not text or a Boolean')
            equal(prompt.call_count, 5)
    elif name == 'sale_success':
        record = dict(p[1], stock=10)
        equal(module.sell_product(record, 3), 1500)
        equal(record['stock'], 7)
        equal(module.sell_product(record, 7), 3500)
        equal(record['stock'], 0)
    elif name == 'sale_invalid':
        for quantity in (0, -2, 11, 2.5, True, False, '3', None):
            record = dict(p[1], stock=10)
            before = record.copy()
            raises(ValueError, lambda: module.sell_product(record, quantity))
            equal(record, before)
        record = dict(p[1], stock=0)
        raises(ValueError, lambda: module.sell_product(record, 1))
        equal(record['stock'], 0)
    elif name == 'validation':
        before = copy.deepcopy(p)
        module.validate_inventory(p)
        equal(p, before)
        module.validate_inventory([])
        module.validate_inventory([dict(p[0], price=0, stock=0, extra='allowed')])
        for invalid in bad_records():
            raises(ValueError, lambda: module.validate_inventory(invalid))
    elif name == 'loading':
        path = work / 'inventory.json'
        equal(module.load_inventory(path), [])
        path.write_text(json.dumps(p), encoding='utf-8')
        equal(module.load_inventory(path), p)
        for invalid in bad_records():
            path.write_text(json.dumps(invalid), encoding='utf-8')
            before = path.read_bytes()
            raises(ValueError, lambda: module.load_inventory(path))
            equal(path.read_bytes(), before)
        for raw, error_type in ((b'{broken', json.JSONDecodeError), (b'\xff', UnicodeError)):
            path.write_bytes(raw)
            raises(error_type, lambda: module.load_inventory(path))
            equal(path.read_bytes(), raw)
        directory = work / 'unreadable-as-file'
        directory.mkdir()
        raises(OSError, lambda: module.load_inventory(directory))
    elif name == 'saving':
        path = work / 'data' / 'inventory.json'
        before_data = copy.deepcopy(p)
        module.save_inventory(path, p)
        equal(json.loads(path.read_text(encoding='utf-8')), p)
        equal(module.load_inventory(path), p)
        equal(p, before_data)
        replacement = [dict(p[0], stock=4)]
        module.save_inventory(path, replacement)
        equal(json.loads(path.read_text(encoding='utf-8')), replacement)
        before = path.read_bytes()
        raises(ValueError, lambda: module.save_inventory(path, [{'id': 1}]))
        equal(path.read_bytes(), before)
        # Fail during the write, after opening. Direct 'w' on the main file
        # truncates it and fails this preservation check; temporary saves pass.
        real_open = open
        class BrokenWriter:
            def __init__(self, handle):
                self.handle = handle
            def __enter__(self):
                return self
            def __exit__(self, *args):
                self.handle.close()
            def write(self, text):
                raise OSError('Simulated disk write failure')
            def __getattr__(self, key):
                return getattr(self.handle, key)
        def fail_writes(file, mode='r', *args, **kwargs):
            handle = real_open(file, mode, *args, **kwargs)
            return BrokenWriter(handle) if any(flag in mode for flag in ('w', 'a', '+')) else handle
        with patch('builtins.open', side_effect=fail_writes), patch('io.open', side_effect=fail_writes):
            raises(OSError, lambda: module.save_inventory(path, p))
        equal(path.read_bytes(), before)
    elif name == 'csv_export':
        path = work / 'exports' / 'inventory.csv'
        rows = [dict(p[0], name='Notebook, "A5"', extra='ignored')]
        module.export_csv(path, rows)
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            equal(reader.fieldnames, ['id', 'name', 'price', 'stock'])
            equal(list(reader), [{'id': '1', 'name': 'Notebook, "A5"', 'price': '200', 'stock': '10'}])
        module.export_csv(path, [])
        with open(path, newline='', encoding='utf-8') as file:
            equal(list(csv.reader(file)), [['id', 'name', 'price', 'stock']])
    else:
        raise ValueError(f'Unknown automated criterion: {name}')
