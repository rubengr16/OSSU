def genPrimes():
    p = 2
    primes = [p]
    j = 0
    while True:
        yield p
        i = p
        while j < len(primes):
            i += 1
            j = 0
            while j < len(primes) and (i % primes[j]) != 0:
                j += 1
        p = i
        primes.append(p)