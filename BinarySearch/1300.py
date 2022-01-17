n = int(input())  # 배열A를 만들기 위해
k = int(input())

start, end = 1, k
result = 0
# 임의의 숫자 m을 골라서 k번째 숫자인지 판단
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, n+1):  # 1~n 각 행 확인
        cnt += min(mid // i, n)  # 각 행에서 임의의 숫자보다 작거나 같은 수의 개수
    if cnt >= k:  # 작거나 같은 수의 개수가 k 보다 크면
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
