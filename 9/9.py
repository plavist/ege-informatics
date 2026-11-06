f = open('99.txt')
from math import prod

count = 0
for line in f:
    l = list(map(int, line.split()))
    tr = [x for x in l if l.count(x) == 2]

    num = 1
    rz = [x for x in l if l.count(x) == 1]
    for k in rz:
        num *= k
    print(tr, rz)
    if len(tr) == 4 and len(rz) == 2 and sum(tr) > sum(rz):
        count += 1

print(count)




