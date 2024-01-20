import sys


def find_divisors(N, K):
    divisors = [i for i in range(1,N+1) if N%i == 0]
    if K < len(divisors):
        return divisors[K-1]
    else:
        return 0

N, K = map(int, sys.stdin.readline().split())
print(find_divisors(N, K))