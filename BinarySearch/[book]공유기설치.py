home, wifi = map(int, input().split())  # 집의 개수, 공유기 개수
array = []
for _ in range(home):
    array.append(int(input()))  # 집의 좌표 입력받기
array.sort()

start = array[1] - array[0]  # 최소 gap
end = array[-1] - array[0]  # 최대 gap
result = 0

while(start <= end):
    mid = (start+end) // 2
    value = array[0]
    cnt = 1
    # 현재 mid(gap)값 이용해 공유기 설치
    for i in range(1, home):
        if array[i] >= value + mid:  # >= 첫번째집 + gap값
            value = array[i]  # 공유기 설치하기
            cnt += 1
    if cnt >= wifi:  # 입력받은 공유기 개수보다 많아질 때, 거리(gap값) 증가시키기
        start = mid + 1
        result = mid  # 최적의 결과를 저장
    else:
        end = mid - 1  # wifi개 이상 공유기 설치 못하는 경우, gap값 감소시키기
print(result)
