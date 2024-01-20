import sys

def find_divisors(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]
    if num > 1 and len(divisors) == 2:
        return True
    else:
        return False

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip()) # 수의 개수 N
    num_arr = list(map(int, sys.stdin.readline().split()))
    print(sum([1 for i in num_arr if find_divisors(i) == True]))