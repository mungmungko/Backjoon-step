import sys

def search_numbers(N, A, M, numbers):
    A.sort()  # 정렬
    results = []
    for num in numbers:
        left, right = 0, N - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == num:
                found = True
                break
            elif A[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        results.append(1 if found else 0)
    return results

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().split()))

    print(*search_numbers(N, A, M, numbers), sep='\n')