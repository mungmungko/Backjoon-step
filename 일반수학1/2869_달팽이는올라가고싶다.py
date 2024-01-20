"""
달팽이는 높이가 V미터인 나무 막대를 올라간다
달팽이는 낮에 A미터 올라갈 수 있다
밤에 잠을 자는 동안 B미터 미끄러진다
정상에 올라간 후에는 미끄러지지 않는다
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성해라
"""
# 달팽이가 하루에 실제로 올라가는 높이 A - B
# 정상에 도달하기 전날까지 달팽이가 올라가야 하는 높이 V - A
# 따라서 총 필요한 일수는 V-A/A-B + 1

import sys
import math
A, B, V = map(int, sys.stdin.readline().split())

days = math.ceil((V-A)/(A-B)) + 1
print(days)