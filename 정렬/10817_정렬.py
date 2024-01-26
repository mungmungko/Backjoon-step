import sys

# numbers = list(map(int, sys.stdin.readline().split()))
# numbers.sort()
# print(numbers[1])
a = "23 10 13 19 23 19 19 16 18 20 20 28 15 15 37 17 19 23 10 28 24 22 13 10 20 20 22 30 12 20 15 30 33 10 15 39"
b = list(map(int, a.split()))
print(sum(b)//60)