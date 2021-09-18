n, m = map(int, input().split())

s = []

def f():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:
            continue
        if s:
            if i < s[-1]:
                continue
        s.append(i)
        f()
        s.pop()

f()
