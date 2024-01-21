"""
봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다
정확하게 N 킬로를 위해서는
5의 배수이거나
3의 배수이거나
0 5 
"""

import sys
N = int(sys.stdin.readline().strip())
bags = 0
while N > 0:
    if N % 5 == 0:
        bags += N // 5
        break
    N -= 3
    bags += 1

print(bags if N >= 0 else -1)