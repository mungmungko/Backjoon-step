import sys
import math

if __name__ == '__main__':
    # 두 자연수 입력
    a, b = map(int, sys.stdin.readline().split())

    # 최대공약수 구하기
    gcd = math.gcd(a, b)

    # 최소공배수 구하기
    lcm = a * b // gcd

    print(gcd)
    print(lcm)