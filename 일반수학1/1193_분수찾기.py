def find_fraction(x):
    line = 0  # 대각선 라인
    end_point = 0  # 해당 라인의 마지막 번호

    while x > end_point:
        line += 1
        end_point += line

    diff = end_point - x
    if line % 2 == 0:  # 짝수 라인 (아래로 이동)
        numerator = line - diff
        denominator = 1 + diff
    else:  # 홀수 라인 (위로 이동)
        numerator = 1 + diff
        denominator = line - diff

    return f"{numerator}/{denominator}"

# 예제 입력
x = int(input())

# 분수 찾기
print(find_fraction(x))