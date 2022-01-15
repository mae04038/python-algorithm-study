# num이 0, 1, 2인 경우 각각의 호출 횟수는 미리 저장해두기
zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num], one[num])


t = int(input())
for _ in range(t):
    fibo(int(input()))
