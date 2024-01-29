import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # DP 테이블 초기화
    dp = [[0]*3 for _ in range(N)]
    dp[0] = costs[0]

    # 각 집을 칠하는 최소 비용 계산
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 집을 칠했을 때의 최소 비용
    print(min(dp[N-1]))