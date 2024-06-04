def podbor(n):
    f = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0 and i != j:
                f.append((i, j))
    parol = ''.join(str(x) + str(y)for x, y in f)
    return parol


for f in range(3, 21):
    kod = podbor(f)
    print(f'{f} - {kod}')
