"""
주어진 약수로부터 원래의 수 N을 찾기 위한 가장 간단한 방법
: 가장 작은 약수와 가장 큰 약수를 곱하기
"""
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    N_arr = list(map(int, sys.stdin.readline().split()))
    N_arr.sort()
    # 가장 작은 약수와 가장 큰 약수 곱하기
    print(N_arr[0]*N_arr[-1])