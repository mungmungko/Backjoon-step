"""
에라토스테네스의 체 알고리즘(특정 범위 내의 모든 소수를 효율적으로 찾는 방법)

기본적으로 2부터 시작하여 특정 숫자의 배수들을 소수가 아닌 것으로 표시,
이미 표시되지 않는 다음 숫자로 넘어가는 방식
"""
import sys

def eratosthenes(M, N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    # int()는 내부의 수치가 소수일 경우 내림을 하여 가장 가까운 정수로 변환한다
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, N + 1, i):
                sieve[j] = False

    for i in range(M, N + 1):
        if sieve[i]:
            print(i)

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    eratosthenes(M, N)