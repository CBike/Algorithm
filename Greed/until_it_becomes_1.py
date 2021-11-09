# n , k 를 공백으로 구분하여 입력받기

n, k = map(int, input().split())

result = 0
# Count 변수

while True:
#     (n == k 로 나누어 떨어지는 수) 가 될때까지 1씩 빼기
    target = (n // k)*k
    result += (n - target)
    n = target
    # N 이 K 보다 작을때 ( 더 이상 나눌 수 없을 떄 ) 반복문 탈출

    if n < k:
        break

    #k로 나누기

    result += 1
    n //= k


result += (n-1)
print(result)



