N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
cnt = 0
arr.sort() # 오름차순 정렬 - 제일 큰 두 수만 이용
for _ in range(M):
    if cnt != K:
        ans += arr[-1]
        cnt += 1
        # print(ans)
    else:
        ans += arr[-2]
        cnt = 0
        # print(ans)

print(ans)

# M커지면 시간초과 날 것 같음

