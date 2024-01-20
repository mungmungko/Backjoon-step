import sys

def return_change(num):
    quarter = num // 25
    num %= 25
    dime = num // 10
    num %= 10
    nickel = num // 5
    penny = num % 5

    return quarter, dime, nickel, penny

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        q, d, n, p = return_change(N)
        print(q, d, n, p)