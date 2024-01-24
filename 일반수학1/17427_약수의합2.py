"""
f(A) = 자연수 A의 약수의 합
g(A) = A보다 작거나 같은 모든 자연수의 약수의 합의 합

각 숫자의 약수를 직접 찾는 대신
각 숫자가 다른 숫자들의 약수로 어떻게 기여하는지 계산
예를 들어, 2는 2, 4, 6, 8의 약수
따라서 2의 기여도는 N/2 만큼(N까지 2의 배수의 개수)
"""
import sys

def calculate_g(N):
    total_sum = 0
    for i in range(1, N+1):
        total_sum += i * (N // i)
    return total_sum

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    print(calculate_g(N))