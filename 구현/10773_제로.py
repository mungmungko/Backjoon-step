import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline().strip())
    stack = []

    for _ in range(K):
        n = int(sys.stdin.readline().strip())
        
        if n == 0:
            stack.pop()
        else:
            stack.append(n)
    
    print(sum(stack))