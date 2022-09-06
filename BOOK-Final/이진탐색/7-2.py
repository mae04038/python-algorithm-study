N = int(input())
data = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if order in data:
        print('yes', end=' ')
    else:
        print('no', end=' ')