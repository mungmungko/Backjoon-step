import sys
# N : 색종이의 수
N = int(sys.stdin.readline().strip())
locates = []
max_x, max_y = 0, 0
size = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    locates.append([x, y])

result = [[0 for _ in range(max_x+10)] for _ in range(max_y+10)]

for dx, dy in locates:
    for i in range(10):
        for j in range(10):
            result[dy+i][dx+j] = 1

for i in range(len(result)):
    for j in range(len(result[0])):
        if result[i][j] == 1:
            size += 1

print(size)