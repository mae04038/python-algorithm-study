# N이 1이 될 때까지 최소횟수
N, K = map(int, input().split())
cnt = 0

while True:
    if N == 1:
        break
    if N%K == 0:
        cnt += 1
        N //= K
    else:
        N -= 1
        cnt += 1
print(cnt)