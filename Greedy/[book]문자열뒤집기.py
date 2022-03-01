data = list(map(int, input()))
cnt0 = 0  # 전부 0으로 만드는 횟수
cnt1 = 0  # 전부 1로 만드는 횟수

if data[0] == 0:
    cnt1 += 1
else:
    cnt0 += 1

for i in range(1, len(data)):
    if data[i] != data[i-1]:
        if data[i] == 0:
            cnt1 += 1
        else:
            cnt0 += 1
print(min(cnt0, cnt1))
