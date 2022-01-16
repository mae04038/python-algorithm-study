n = int(input())  # 집의 개수
RGB = []
for _ in range(n):
    RGB.append(list(map(int, input().split())))

# 빨간집을 골랐을 때, 초록집을 골랐을 때, 파란집을 골랐을 때 각각의 경우 따져서
# 최종적으로 비용이 적게드는 것 고르기
for i in range(1, n):
    # 빨간집
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    # 초록집
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    # 파란집
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]
print(min(RGB[n-1]))
