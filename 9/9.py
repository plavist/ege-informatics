f = open('9.txt', 'r')
counter = 0
for line in f:
    l = list(map(int, line.strip().split()))
    if len(l) == len(set(l)) and max(l) * 2 + min(l) * 2 > sum(l) - max(l) - min(l):
        print(set(l))
        counter += 1
print(counter)


