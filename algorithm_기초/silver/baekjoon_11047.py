n, money = map(int, input().split())
coin = []
cnt = 0

for i in range(n):
    coin.append(int(input()))


while money > 0:
    if money % coin[-1] != money:
        cnt += money // coin[-1]
        money = money % coin[-1]
    coin.pop()

print(cnt)
