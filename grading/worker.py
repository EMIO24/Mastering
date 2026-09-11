"""Private worker: imports a copied student file, never the original path."""
import contextlib
import importlib.util
import json
import sys
from pathlib import Path
from unittest.mock import patch
# Isolated Python omits the script directory from its import search path.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from week1 import check


class LimitedOutput:
    """Keep accidental print loops from accumulating unlimited captured text."""
    def __init__(self):
        self.text = ''
    def write(self, text):
        self.text += text[:max(0, 2000-len(self.text))]
        return len(text)
    def flush(self):
        pass


def main():
    source, config, output = map(Path, sys.argv[1:])
    rubric = json.loads(config.read_text(encoding='utf-8-sig'))
    criteria = [item for item in rubric['criteria'] if item['mode'] == 'auto']
    result = {}
    log = LimitedOutput()
    # Add the temporary assignment directory to permit sibling module imports.
    sys.path.insert(0, str(source.parent))
    try:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with patch('builtins.input', side_effect=EOFError('Put interactive startup under if __name__ == "__main__"')):
                spec = importlib.util.spec_from_file_location('student_submission', source)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
    except BaseException as error:
        message = f'Cannot import submission: {type(error).__name__}: {error}'
        result = {item['id']: {'passed': False, 'feedback': message[:2000]} for item in criteria}
    else:
        for item in criteria:
            work = output.parent / ('case-' + item['id'])
            work.mkdir()
            try:
                with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
                    with patch('builtins.input', side_effect=EOFError('Unexpected interactive input in a function check')):
                        check(item['id'], module, work)
            except BaseException as error:
                result[item['id']] = {'passed': False, 'feedback': f'{type(error).__name__}: {error}'[:2000]}
            else:
                result[item['id']] = {'passed': True, 'feedback': 'Passed the automated behaviour cases.'}
    output.write_text(json.dumps(result, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
