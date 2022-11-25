n = int(input())
coins = list(map(int, input().split()[:n]))

coins = sorted(coins)
cou = 0
l = len(coins)
s = 0
for i in range(l):
    a = coins.pop()
    s += a
    cou += 1
    if s > sum(coins):
        break

print(cou)
