n = int(input())  # 수열의 크기
A = list(map(int, input().split()))
reverseA = A[::-1]  # 수열A를 거꾸로 해서 증가하는 거 구해야 감소하는 수열 구하기 가능

increase = [1 for i in range(n)]  # 가장 긴 증가하는 부분 수열 길이
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:  # i인덱스 이전 요소들이랑 i인덱스 요소랑 비교
            # print("i값:%d j값 :%d" % (i, j))  # test
            increase[i] = max(increase[i], increase[j]+1)  # 증가하는 수열
            # print("길이:%d" % increase[i])  # test

decrease = [1 for i in range(n)]  # 가장 긴 감소하는 부분 수열 길이
for i in range(n-1, -1, -1):  # n-1, n-2, ..., 0
    for j in range(n-1, i, -1):  # i인덱스 뒤의 요소들
        if A[i] > A[j]:  # i번째가 제일 커야 감소하는 수열
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[i] - 1
print(max(result))
