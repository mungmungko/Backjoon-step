# 나이순, 나이가 같으면 가입한 순으로 한 줄에 한명씩 나이와 이름을 공백으로 구분하여 출력
"""
파이썬의 기본 정렬 'sort()'함수는 안정적인 정렬(stable sort)방식을 사용하여
같은 키 값을 가진 요소들의 상대적 순서가 정렬 전과 후에도 변하지 않는다
> 따라서, 나이(age)만을 기준으로 정렬하면 된다.
"""
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    members = []
    for _ in range(N):
        age, name = sys.stdin.readline().split()
        members.append((int(age), name))
    members.sort(key=lambda x: (x[0]))

    for age, name in members:
        print(age, name)