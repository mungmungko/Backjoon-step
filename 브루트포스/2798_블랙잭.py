import sys
import itertools

def blackjack(N, M, cards):
    max_sum = 0
    for comb in itertools.combinations(cards, 3):
        card_sum = sum(comb)
        if card_sum <= M:
            max_sum = max(max_sum, card_sum)
    return max_sum


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    
    print(blackjack(N, M, cards))