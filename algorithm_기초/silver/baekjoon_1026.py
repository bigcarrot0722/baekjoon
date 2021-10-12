s = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()
b.reverse()

sum = 0
for i in range(s):
    sum += a[i] * b[i]

print(sum)
