import sys
# 단어들을 입력 받음
words = [sys.stdin.readline().strip() for _ in range(5)]

# 가장 길이가 긴 단어의 길이를 저장
max_length = max(len(word) for word in words)

# 출력할 문자를 저장할 배열
result = []

for k in range(max_length):
    for word in words:
        if len(word) > k:
            result.append(word[k])
print(''.join(result))