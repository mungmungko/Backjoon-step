import sys

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num >= 2:
        return fibonacci(num-1) + fibonacci(num-2)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(fibonacci(n))
