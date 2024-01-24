import sys

def find_smallest(n):
    number = 1
    length = 1

    while True:
        if number % n == 0:
            return length
        
        number = number * 10 + 1
        length += 1

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        if not line:  # 빈 문자열 체크
            break
        n = int(line)
        print(find_smallest(n))