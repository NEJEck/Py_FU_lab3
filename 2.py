n = int(input())
if n >= 2:
    i = 2
    while n % i != 0:
        i += 1
    print(i)
else:
    print("Введите число не меньше 2")
