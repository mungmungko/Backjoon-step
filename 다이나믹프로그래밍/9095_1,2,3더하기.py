import sys

def ways_to_sum(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return ways_to_sum(n-1)+ways_to_sum(n-2)+ways_to_sum(n-3)

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        print(ways_to_sum(int(sys.stdin.readline().strip())))