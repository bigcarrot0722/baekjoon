import sys

n = int(input())
ls = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
dp_2 = []
kk = []

for i in range(n):
    k = 0
    for j in range(i):
        if ls[j] < ls[i]:
            if dp[i] < dp[j] + 1:
                k = j
            dp[i] = max(dp[i], dp[j] + 1)
    dp_2.append(k)
            
print(max(dp))

a = dp.index(max(dp))

while len(kk) != max(dp):
    kk.append(ls[a])
    a = dp_2[a]
    
kk.reverse()

for i in kk:
    print(i, end=" ")
