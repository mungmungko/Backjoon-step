"""
'replace' 함수는 찾는 문자열이 없으면 아무런 변화도 일으키지 않는다
"""

import sys
word = sys.stdin.readline().strip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for croatian_alphabet in croatia:
    word = word.replace(croatian_alphabet, '0')

print(len(word))