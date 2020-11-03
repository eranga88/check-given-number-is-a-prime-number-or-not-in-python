import math

def prime_checker(N):
    if N == 1:
        return False

    max = math.floor(math.sqrt(N))

    for i in range(2,max + 1):
        if N%i == 0:
            return False
    return True


data_base = []

for i in range(2,1000):
    if prime_checker(i):
        data_base.append(i)

print(data_base)
