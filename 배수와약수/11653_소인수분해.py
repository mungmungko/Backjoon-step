import sys

def prime_factorization(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n**0.5)+1, 2): # 3부터 홀수만 판단
        while n % i == 0:
            factors.append(i)
            n = n // i
        
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == '__main__':
    num = int(sys.stdin.readline().strip())
    for x in prime_factorization(num):
        print(x)