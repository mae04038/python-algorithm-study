N = int(input()) #거슬러줘야할 돈
coins = [500, 100, 50, 10]
ans = 0
for coin in coins:
    ans += N // coin
    N %= coin
print(ans)