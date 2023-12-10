def summ(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiplicate(a, b):
    return a * b


def dedenie(a, b):
    return a / b


a = int(input("Значение 1 переменной: "))
b = int(input("Значение 2 переменной: "))
valid_operators = ['+', '-', '*', '/']
c = input("Выберите оператор: ").strip()
if c not in valid_operators:
    print("Неверный оператор.")
    exit()
if c == "+":
    res = summ(a, b)
elif c == "-":
    res = minus(a, b)
elif c == "*":
    res = multiplicate(a, b)
else:
    res = dedenie(a, b)

print(res)
