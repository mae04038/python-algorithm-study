N = int(input()) # 0 <= N <= 23
ans = 0
for hour in range(N+1):
    for min in range(60):
        for sec in range(60):
            time = str(hour)+str(min)+str(sec)
            if time.count('3') > 0:
                ans += 1

print(ans)