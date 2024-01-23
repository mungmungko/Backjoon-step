# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
import sys

def tiling(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2

    # 점화식을 통한 dp 테이블 채우기
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    return dp[n]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(tiling(n))