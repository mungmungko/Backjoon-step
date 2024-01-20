"""
첫번째 숫자가 두번째 숫자의
약수라면 factor
배수라면 multiple
둘 다 아니라면 neither
"""

import sys

for line in sys.stdin:
    a, b = map(int, line.split())

    if a == 0 and b == 0:  # 입력이 0 0이면 반복 종료
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")