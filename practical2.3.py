"""WAP to generate first 'n' numbers using Functions"""
def gen_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes
n = int(input("Enter the number of prime numbers to generate: "))
print("The first", n, "prime numbers are:", gen_primes(n))
