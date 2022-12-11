# 입력을 위한 전형적인 소스코드 1)

# 데이터의 개수 입력
n = int(input())
print(n)

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
print(data)

data.sort(reverse=True)
print(data)

# 입력을 빠르게 하기 위한 sys 라이브러리
import sys

# 문자열 입력받기
data = sys.stdin