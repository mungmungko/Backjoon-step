import sys

def fibonacci_count(n):
    # # 0과 1이 출력되는 횟수를 저장할 배열 초기화
    zero_count = [1, 0] + [0] * (n - 1)
    one_count = [0, 1] + [0] * (n - 1)

    for i in range(2, n+1):
        zero_count[i] = zero_count[i-1] + zero_count[i-2]
        one_count[i] = one_count[i-1] + one_count[i-2]
    
    return zero_count[n], one_count[n]


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        num = int(sys.stdin.readline().strip())
        print(*fibonacci_count(num))