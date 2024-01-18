import sys
max_value = 0
i, j = 0, 0

for k in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    max_temp = max(row)
    if max_temp >= max_value:
        max_value = max_temp
        i, j = k, row.index(max_value)

print(max_value)
print(i+1, j+1)