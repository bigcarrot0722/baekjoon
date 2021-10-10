a = int(input())
num = list(map(int, input().split()))
k = int(input())
cnt = 0
key = 0
num.sort()

for i in range(a):
    if k < num[i]:
        key = i
        break

if i == 0:
    min = 1
else:
    min = num[i-1]
max = num[i]

for i in range(min + 1, k + 1):
    for j in range(k, max):
        if i < j:
            cnt += 1

print(cnt)
