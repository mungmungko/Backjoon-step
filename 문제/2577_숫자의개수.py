import sys
from collections import Counter
sum = 1
for _ in range(3):
    sum = sum * int(sys.stdin.readline().strip())

count = Counter(str(sum))

for i in range(10):
    print(count[str(i)])