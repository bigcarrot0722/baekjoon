import sys

n, k = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls.sort()
print(ls[k - 1])
