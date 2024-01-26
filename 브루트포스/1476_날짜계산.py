"""
지구(E): 1에서 15까지
태양(S): 1에서 28까지
달(M): 1에서 19까지
"""
import sys

def calculate_year(E, S, M):
    e, s, m = 1, 1, 1
    year = 1

    while True:
        if e == E and s == S and m == M:
            return year
        
        e, s, m = e+1, s+1, m+1
        year += 1
        
        if e > 15:
            e = 1
        
        if s > 28:
            s = 1
        
        if m > 19:
            m = 1

if __name__ == '__main__':
    E, S, M = map(int, sys.stdin.readline().split())
    print(calculate_year(E, S, M))