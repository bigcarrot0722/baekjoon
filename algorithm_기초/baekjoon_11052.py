import sys

n = int(input())
dp = list(map(int, sys.stdin.readline().split()))
dp_old = dp

if n > 1:
    if dp[1] < dp[0] + dp[0]:
        dp[1] = 2 * dp[0]

if n > 3:
    for i in range(2, n):
        for j in range(i):
            if dp[i] < dp[j] + dp_old[i - j - 1]:
                dp[i] = dp[j] + dp_old[i - j - 1]

print(dp[n - 1])
