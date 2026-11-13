def f(x):
    if x == 141:
        return 1
    elif x > 141:
        return 0
    c = f(x+1)

    tens = x // 10 % 10
    units = x % 10

    if tens < units:

        c += f(x // 100 * 100 + units * 10 + tens)

    return c

print(f(100))