"""
동적 프로그래밍 접근 방식은
각 숫자에 도달하는 데 필요한 최소 연산 횟수를 점진적으로 계산하고,
이 정보를 배열에 저장하여 사용한다.

각 숫자에 대해 1을 빼는 연산, 2로 나누는 연산, 3으로 나누는 연산 중
최소 횟수를 선택하여 해당 숫자에 대한 최소 연산 횟수를 결정한다
"""
import sys

def min_operations_to_one(N):
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        dp[i] = dp[i-1] + 1 # 1을 빼는 연산
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1) # 2로 나누는 연산
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1) # 3으로 나누는 연산
        
    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    print(min_operations_to_one(N))