import sys

# 보드의 가로 및 세로 방향으로 연속된 사탕의 개수를 세는 함수
def count_candy(board):
    n = len(board)
    max_count = 0
    for i in range(n):
        count_row = 1
        count_col = 1
        for j in range(1, n):
            # 가로 방향 확인
            if board[i][j] == board[i][j-1]:
                count_row += 1
                max_count = max(max_count, count_row)
            else:
                count_row = 1
            
            # 세로 방향 확인
            if board[j][i] == board[j-1][i]:
                count_col += 1
                max_count = max(max_count, count_col)
            else:
                count_col = 1

    return max_count

# 보드의 각 위치에서 사탕을 교환한 뒤 다시 원래대로 돌려놓음
def solve(board):
    n = len(board)
    answer = 0
    for i in range(n):
        for j in range(n):
            # 가로 방향 교환
            if j + 1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                answer = max(answer, count_candy(board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # 세로 방향 교환
            if i + 1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                answer = max(answer, count_candy(board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

    return answer


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    candies = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(solve(candies))