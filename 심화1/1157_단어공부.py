"""
<문제>
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성 하시오.
단, 대문자와 소문자를 구분하지 않는다.
"""
import sys
from collections import Counter
# 단어를 받아서 대문자로 변환
word = sys.stdin.readline().strip().upper()
# 글자별 빈도 수 계산
counter = Counter(word)
# 가장 많이 사용된 알파벳 찾기
most_common = counter.most_common(2) # [('E', 5), ('Y', 2)]

# 'most_common' 함수의 결과 리스트의 길이가 1 이하인 경우,
# 즉 리스트에 요소가 하나만 있거나 비어있는 경우에는 'most_common[0][1]' 이후의
# 비교를 수행할 필요가 없다
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print('?')
else:
    print(most_common[0][0])