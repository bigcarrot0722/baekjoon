import sys

def binary_search(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if n_ls[mid] == target:
        return 1
    elif n_ls[mid] > target:
        return binary_search(target, start, mid -1 )
    else:
        return binary_search(target, mid + 1, end)
    

n = int(sys.stdin.readline().rstrip())
n_ls = list(map(int, sys.stdin.readline().split()))
n_ls.sort()

m = int(sys.stdin.readline())
m_ls = list(map(int, sys.stdin.readline().split()))

for i in m_ls:
    print(binary_search(i, 0, n - 1), end = " ")


