import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    meetings = []
    for _ in range(N):
        # 회의 시작 시간, 회의 끝나는 시간
        x, y = map(int, sys.stdin.readline().split())
        meetings.append((x, y))
    
    # 끝나는 시간을 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    end_time = 0

    for start, end in meetings:
        if start >= end_time:
            end_time = end
            count += 1

    print(count)