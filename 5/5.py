for N in range(1, 1000000):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = f'11{b}11'
    else:
        b = f'1{b}00'
    R = int(b, 2)
    if R > 95:
        print(R)
        break