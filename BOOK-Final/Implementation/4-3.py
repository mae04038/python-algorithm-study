# 총 8가지로 이동 가능
dx = [-1, 1, -1, 1, 2, 2, -2, -2] # 세로
dy = [2, 2, -2, -2, -1, 1, -1, 1] # 가로

now = str(input())
garo = int(ord(now[0]) - 96) #알파벳
sero = int(now[1]) #숫자

ans = 0

for i in range(8):
    nx = sero + dx[i]
    ny = garo + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        ans += 1
print(ans)
