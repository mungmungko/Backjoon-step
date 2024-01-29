import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().split())
    # A+B*n < C*n
    # A//(C-B)
    if B >= C: # B가 C보다 크거나 같은 경우 손익분기점은 존재하지 않음
        print(-1)
    else:
        print(A//(C-B)+1)