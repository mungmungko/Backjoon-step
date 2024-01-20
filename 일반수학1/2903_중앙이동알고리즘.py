import sys

# 정사각형의 한 변의 길이
def calculate_points(n):
    rec = [(n-2*i)*4 for i in range(n//2)]
    print(sum(rec)+1)


# 예제 입력
n = int(sys.stdin.readline().strip())
# 정사각형 한 변의 길이 2 > 4 > 8 > 16 > 32
# 2*n
length_of_one_side = 2**n
calculate_points(length_of_one_side)