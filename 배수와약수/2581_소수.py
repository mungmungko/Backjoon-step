import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    M = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    result = []

    for i in range(M, N+1):
        if is_prime(i) == True:
            result.append(i)
    
    if result:
        print(sum(result))
        print(min(result))
    else:
        print(-1)