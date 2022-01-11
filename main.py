def a(n):
    if n == 1:
        return 1
    if n > 1:
        return n - a(a(n - 1))
    if n == 0:
        return False


n = int(input('Введите значение n: '))
print(a(n))
