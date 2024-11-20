n = 7

a = [[(((7 - j) - i) if j < 7 - i else 0) for i in range(n)] for j in range(n)]

for r in a:
    print(''.join(map(str, r)))
