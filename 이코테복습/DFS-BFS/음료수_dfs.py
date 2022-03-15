'''
구멍 뚫려 있는 부분 : 0
칸막이가 존재하는 부분 : 1
각각 이동하면서 상하좌우 확인 -> 방문처리
만들 수 있는 아이스크림의 개수 출력
'''

n, m = map(int, input().split()) #n:세로 m:가로
ice = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x > n or y < 0 or y > m:
        return False
        
    if ice[x][y] == 0: #이동가능, 아이스크림 만들기 가능
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

#모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs수행
        if dfs(n, m) == True:
            result += 1

dfs(0, 0)