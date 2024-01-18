import sys

def is_group_word(word):
    seen = set()
    prev_char = ''

    for char in word:
        if char != prev_char and char in seen:
            return False
        seen.add(char)
        prev_char = char
    
    return True

N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
print(sum([1 for x in words if is_group_word(x) == True]))