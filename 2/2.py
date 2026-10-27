from itertools import product

def f(w, x, y, z):
    return ((x == (not y)) <= (not ((not w) or x))) or (not z)

for a, b, c, d in product([0, 1], repeat=4):
    if f(a, b, c, d) == 0:
        print(a, b, c, d)
