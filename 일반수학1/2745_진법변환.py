"""
int() 함수는 두 번째 매개변수로 기수(base)를 입력받아
해당 기수의 문자열을 10진수로 변환할 수 있다.
"""
import sys

def convert_to_decimal(num_str, base):
    return int(num_str, base)

N, B = sys.stdin.readline().split()
print(convert_to_decimal(N, int(B)))