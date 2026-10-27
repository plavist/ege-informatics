from itertools import permutations, product

a = "АКЦЕНТ"

for i, x in enumerate(product(sorted(a), repeat=5), start=1):
    if x[0] not in 'АЕК' and x.count('Т') > 0:
        print(i, x)
        break