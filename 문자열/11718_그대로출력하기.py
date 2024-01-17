"""
sys.stdin은 Python에서 표준 입력 스트림을 나타냄

1.read(size=-1):
이 메서드는 파일의 내용을 지정된 크기만큼 읽어서 문자열로 반환합니다.
size 매개변수가 주어지지 않거나 -1로 설정된 경우, 파일의 현재 위치부터 파일 끝까지의 모든 데이터를 읽습니다.
파일의 크기가 큰 경우, read() 메서드는 메모리 문제를 일으킬 수 있습니다.

2.readline(size=-1):
이 메서드는 파일에서 한 줄을 읽어서 문자열로 반환합니다.
size 매개변수가 주어지면, 최대 size 바이트만큼의 데이터를 읽거나 줄의 끝에 도달할 때까지 읽습니다.
줄바꿈 문자('\n')도 문자열의 일부로 포함됩니다.
파일의 끝에 도달하면 빈 문자열('')을 반환합니다.

3.readlines(hint=-1):
이 메서드는 파일의 모든 줄을 읽어서 각 줄을 요소로 갖는 리스트를 반환합니다.
hint 매개변수가 주어지면, 그만큼의 문자를 대략적으로 읽지만, 파일의 줄 구분을 완전히 존중하여 마지막 줄을 완전히 읽어들입니다.
readlines()는 파일의 모든 줄을 메모리에 로드하므로, 파일의 크기가 매우 큰 경우 메모리 문제가 발생할 수 있습니다.
"""
import sys

for line in sys.stdin: # 사용자가 입력을 중단할 때까지 계속해서 줄 단위로 입력을 읽는다
    # 입력된 각 줄에 대한 처리
    print(line, end='')