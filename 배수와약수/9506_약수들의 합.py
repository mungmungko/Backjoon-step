import sys

def check_perfectnumber(N): # 완전수인지 판단하는 함수
    divisors = [i for i in range(1,N) if N%i == 0]
    divisors_str = [str(i) for i in divisors]
    if N == sum(divisors):
        return f"{N} = "+" + ".join(divisors_str)
    else:
        return f"{N} is NOT perfect."

if __name__ == '__main__':
    while True:
        n = int(sys.stdin.readline().strip())
        if n == -1:
            break
        else:
            print(check_perfectnumber(n))