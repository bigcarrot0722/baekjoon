n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls = list(set(ls))
ls.sort()

s = []

def f():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(0, n):
        if ls[i] in s:
            continue
        s.append(ls[i])
        f()
        s.pop()
f()
