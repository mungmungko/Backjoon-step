import sys
from itertools import combinations

def find_seven(dwarves):
    for seven_dwarves in combinations(dwarves, 7):
        if sum(seven_dwarves) == 100:
            return sorted(seven_dwarves)

if __name__ == '__main__':
    dwarves = [int(sys.stdin.readline().strip()) for _ in range(9)]
    print(*find_seven(dwarves), sep='\n')