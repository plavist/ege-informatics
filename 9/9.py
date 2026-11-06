f = open('99.txt')
from math import prod
count = 0
for line in f:
    l = list(map(int, line.split()))
    tr = [x for x in l if l.count(x) == 3]
    rz = [x for x in l if l.count(x) == 1]
    if len(tr) == 3 and len(rz) == 3 and tr[0] ** 3 < prod(rz):
        count += 1


print(count)




