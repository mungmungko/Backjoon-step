# 1 > 2 ~ 7 > 8 ~ 19 > 20 ~ 37 > 38 ~ 61
# 1 > 6 > 12 > 18 > 24
# 1 > 7 > 19 > 37 > 61
import sys
n = int(sys.stdin.readline().strip())
flag = 1
while n > 1:
    n -= 6*(flag)
    flag += 1

print(flag)