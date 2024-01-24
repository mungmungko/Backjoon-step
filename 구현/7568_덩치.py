import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    members = []
    result = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        members.append((x, y))
    
    for x, y in members:
        sum_of_bigger = 0
        for p, q in members:
            if x < p and y < q:
                sum_of_bigger += 1
        result.append(sum_of_bigger+1)
    
    print(*result)