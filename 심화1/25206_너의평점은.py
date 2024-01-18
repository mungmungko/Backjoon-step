import sys
if __name__ == '__main__':
    level = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
             'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
    
    subjects = 0
    sum_cl = 0
    sum_c = 0
    for _ in range(20):
        s, c, l = sys.stdin.readline().split()
        if l != 'P':
            sum_c += float(c)
            sum_cl += level[l]*float(c)
        
    print(round(sum_cl/sum_c,6))