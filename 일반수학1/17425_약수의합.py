"""
f(A) = 자연수 A의 약수의 합
g(A) = A보다 작거나 같은 모든 자연수의 약수의 합의 합

각 테스트 케이스마다 'calculate_g' 함수를 호출하게 되면
N의 최댓값이 1,000,000인 경우 최악의 시간 복잡도는 O(T * N)이 되어버림
이 문제를 해결하기 위해서는 모든 테스트 케이스에 대한 계산을 한 번에 수행하는 방식으로 코드 실행
1부터 N의 최댓값까지 각 숫자에 대한 g(N)값을 미리 계산해두고
각 테스트케이스에서는 계산된 값을 바로 참조
"""
def precalculate_g(max_N):
    f_values = [0] * (max_N+1)
    g_values = [0] * (max_N+1)

    for i in range(1, max_N + 1):
        for j in range(i, max_N + 1, i):
            f_values[j] += i
        g_values[i] = g_values[i-1] + f_values[i]
    return g_values

n = int(input())
max_N = 1000000
g_values = precalculate_g(max_N)
divList = list()
for i in range(n):
    a = int(input())
    divList.append(a)
for i in divList:
    print(g_values[i])