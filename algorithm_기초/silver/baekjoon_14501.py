import sys

n = int(sys.stdin.readline())
schedule = []
cnt = [0] * n
for _ in range(n):
    ti, pi = map(int, sys.stdin.readline().split())
    schedule.append([ti, pi])

for i in range(n - 1, -1,-1):
    if i == n - 1:
        if schedule[i][0] == 1:
            cnt[i] = schedule[i][1]
    else:
        if i + schedule[i][0] <= n:
            if i+ schedule[i][0] == n:
                cnt[i] = schedule[i][1]
            else:
                cnt[i] = schedule[i][1] + cnt[i + schedule[i][0]]
        cnt[i] = max(cnt[i], cnt[i+1])

print(cnt[0])

