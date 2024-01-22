"""
lambda x: (len(x), x)는 람다 함수를 정의 합니다.

이 함수는 각 단어 'x'를 입력으로 받고,
(len(x), x)라는 튜플을 반환합니다.

sort 메서드는 이 튜플을 기준으로 각 요소들을 정렬합니다.
튜플의 첫 번째 요소인 len(x)가 주요 정렬 기준이 됩니다.

만약 두 단어의 길이가 같다면,
튜플의 두 번째 요소인 'x'(즉, 단어 자체)가 정렬의 부차적 기준이 됩니다.
"""

import sys
    
if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for _ in range(N)]
    
    words = list(set(words)) # 중복된 단어는 하나만 남기고 제거
    words.sort(key=lambda x: (len(x), x))
    
    for word in words:
        print(word)