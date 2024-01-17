import sys

def alphabet_num(c):
    if c in ['A','B','C']:
        return 3
    elif c in ['D','E','F']:
        return 4
    elif c in ['G','H','I']:
        return 5
    elif c in ['J','K','L']:
        return 6
    elif c in ['M','N','O']:
        return 7
    elif c in ['P','Q','R','S']:
        return 8
    elif c in ['T','U','V']:
        return 9
    elif c in ['W','X','Y','Z']:
        return 10
    else:
        return 0

word = sys.stdin.readline().strip()
print(sum(alphabet_num(c) for c in word))