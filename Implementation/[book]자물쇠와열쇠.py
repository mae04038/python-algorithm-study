key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# 2차원 리스트 90도 회전


def rotate_matrix_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠부분 합이 다 1인지 확인


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True

    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 바꾸기
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # key 회전시켰을 때 4가지 방향 다 확인
    for rotation in range(4):
        key = rotate_matrix_90(key)  # 90도 회전시키기
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 key 끼워넣기 -> 자물쇠 더하기 key 합이 1인지 확인
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:  # 새로운 자물쇠에 열쇠가 정확히 맞는지 확인
                    return True
                # 자물쇠에서 열쇠 다시 빼기 - 방향 다 확인해야 하기 때문에
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return answer


solution(key, lock)
