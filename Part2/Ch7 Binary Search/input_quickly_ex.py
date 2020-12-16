# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편
# 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려 시간 초과 될 수도
# 이 때 sys 라이브러리의 readline()함수 이용하면 시간 초과 피할 수 있음
# sys 라이브러리르 사용할 때는 한 줄 입력받고 나서 rstrip()함수 꼭 써야함!
# 이는 readline()의 경우 enter가 줄 바꿈 기호로 입력되므로

import sys 

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data) 