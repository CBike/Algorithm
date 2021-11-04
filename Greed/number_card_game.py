# N , M 을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

result = 0
# 한 줄씩 공백으로 구분하여 정수 받기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수' 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용한 답안

# N, M을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    result = 0
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value =min(min_value, a)

    #가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)