import sys

def is_valid_vps(parenthesis):
    count = 0
    for char in parenthesis:
        if char == '(':
            count += 1
        else:  # char == ')'
            count -= 1
        if count < 0: # count가 0 밑으로 떨어지면 안됨
            return "NO"
    return "YES" if count == 0 else "NO"


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        print(is_valid_vps(sys.stdin.readline().strip()))