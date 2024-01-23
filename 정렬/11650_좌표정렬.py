import sys

def sort_coordinates(coordinates):
    # x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순으로
    coordinates.sort(key=lambda x: (x[0], x[1]))

    # x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 감소하는 순서로 정렬
    # coordinates.sort(key=lambda x: (x[0], -x[1]))
    
    return coordinates

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    coordniates = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coordniates.append((x, y))
    
    sort_coordinates(coordniates)

    for x, y in coordniates:
        print(x, y)