import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    times = list(map(int, sys.stdin.readline().split()))
    times.sort() # 시간들을 오름차순으로 정렬
    total_time = 0
    accumulated_time = 0

    for time in times:
        accumulated_time += time
        total_time += accumulated_time
    
    print(total_time)