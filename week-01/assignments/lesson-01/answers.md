# Number 1








# Number 5
Dictionaries can hold data in keys and values, hence we can store data's with values directly without creating a lot of variables to tempoaryly store data

List can hold series of data types including data structures, hence we can use it to store datas of different types and structures in one variable.

## Exercise 9: Repair a function that only prints — 5 points
def total(price, quantity):
    print(price * quantity)

answer = total(200, 3)
print(answer)

Explain why the function can display `600` while `answer` receives `None`. Think of a cashier announcing a total but handing back no receipt.

The print function is displaying the value of 200 * 3, not returning a value. We cannot assign a print to a variable
