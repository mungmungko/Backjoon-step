import sys
from itertools import combinations

def find_seven(dwarves):
    for seven_dwarves in combinations(dwarves, 7):
        if sum(seven_dwarves) == 100:
            return sorted(seven_dwarves)

if __name__ == '__main__':
    dwarves = [int(sys.stdin.readline().strip()) for _ in range(9)]
    seven_dwarves = find_seven(dwarves)
    print(*seven_dwarves, sep='\n')