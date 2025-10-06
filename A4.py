a = int(input("Введите 1-ое число"))
b = int(input("Введите 2-ое число "))
result = [a, b][a <= b]
result = ("Максимум:", result)
print(result)