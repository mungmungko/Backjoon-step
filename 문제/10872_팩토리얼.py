import sys

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)
        

N = int(sys.stdin.readline().strip())
print(factorial(N))