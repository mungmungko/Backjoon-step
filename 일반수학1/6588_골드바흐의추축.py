import sys

def sieve_of_eratosthenes(max_num):
    is_prime = [True for _ in range(max_num + 1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False
    return [i for i in range(2, max_num) if is_prime[i]]

def goldbach_conjecture(n, primes, is_prime):
    for prime in primes:
        if prime > n:
            break
        if is_prime[n - prime]:
            return f"{n} = {prime} + {n - prime}"
    return "Goldbach's conjecture is wrong."

# 메인 로직
if __name__ == '__main__':
    max_num = 1000000
    primes = sieve_of_eratosthenes(max_num)
    is_prime = [False] * (max_num + 1)
    for prime in primes:
        is_prime[prime] = True

    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        print(goldbach_conjecture(n, primes, is_prime))