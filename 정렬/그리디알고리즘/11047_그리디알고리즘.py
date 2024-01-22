import sys

def min_coins(N, K, coins):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += K // coin
        K %= coin
        if K == 0:
            break
    return count

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(min_coins(N, K, coins))