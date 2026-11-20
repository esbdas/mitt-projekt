def ar_primtal(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Skriver bara ut (och gör mellanslag) om talet faktiskt är ett primtal
for n in range(1, 10000000001):
    if ar_primtal(n):
        print(n, end = " ")
