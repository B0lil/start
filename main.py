a = int(input("Значение 1 переменной: "))
b = int(input("Значение 2 переменной: "))
valid_operators = ['+', '-', '*', '/']
c = input("Выберите оператор: ").strip()
if c not in valid_operators:
    print("Неверный оператор.")
    exit()
if c == "+":
    res = (a + b)
elif c == "-":
    res = (a - b)
elif c == "*":
    res = (a * b)
else:
    res = (a / b)

print(res)
