sieve = [True] * 100

for i in range (len(sieve)):
    x = 2
    while True
        if (i + 2) * x < len(sieve):
            sieve[(i + 2) * x] = False
        else:
            break
        x = x + 1
