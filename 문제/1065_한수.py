import sys

def check_han_number(num):
    if num < 100:
        return True
    else:
        str_num = str(num)
        if int(str_num[2]) - int(str_num[1]) == int(str_num[1]) - int(str_num[0]):
            return True
        else:
            return False

N = int(sys.stdin.readline().strip())

if N == 1:
    print(1)
else:
    sum = 0
    for i in range(1,N+1):
        if check_han_number(i):
            sum += 1
    print(sum)