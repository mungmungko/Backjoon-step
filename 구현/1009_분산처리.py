import sys

def compute_patterns():
    patterns = [[] for _ in range(9)]
    for i in range(1, 10):
        temp = i
        while temp not in patterns[i-1]:
            patterns[i-1].append(temp)
            temp = (temp*i) % 10
    return patterns

if __name__ == '__main__':
    patterns = compute_patterns()
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        a %= 10 # 마지막 자리 숫자만 고려
        if a == 1:
            print(1)
        elif a == 0:
            print(10)
        else:
            pattern = patterns[a-1]

            # 패턴이 반복되는 것을 고려하여 인덱스 계산
            idx = b % len(pattern)

            # 결과가 0이면 실제 컴퓨터 번호는 10
            print(pattern[idx-1])