import sys
N = int(sys.stdin.readline().strip())
result = [int(sys.stdin.readline().strip()) for _ in range(N)]
result.sort()

for x in result:
    print(x)