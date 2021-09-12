n = int(input())
dp = [0] * 100001
dp_1 = [0] * 100001
dp_2 = [0] * 100001
dp_3 = [0] * 100001
dp[1] = 1
dp[2] = 1
dp[3] = 3
dp_1[1] = 1
dp_2[2] = 1
dp_1[3] = 1
dp_2[3] = 1
dp_3[3] = 1

for i in range(4, 100001):
    dp_1[i] = (dp[i - 1] - dp_1[i - 1]) % 1000000009
    dp_2[i] = (dp[i - 2] - dp_2[i - 2]) % 1000000009
    dp_3[i] = (dp[i - 3] - dp_3[i - 3]) % 1000000009
    dp[i] = dp_1[i] + dp_2[i] + dp_3[i]
        

    
for k in range(n):
    num = int(input())
    print(dp[num] % 1000000009)
