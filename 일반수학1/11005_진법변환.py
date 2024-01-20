import sys

def convert_from_decimal(num, base):
    conversion = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while num > 0:
        result = conversion[num % base] + result
        num //= base
    
    return result
    
N, B = map(int, sys.stdin.readline().split())
print(convert_from_decimal(N, B))