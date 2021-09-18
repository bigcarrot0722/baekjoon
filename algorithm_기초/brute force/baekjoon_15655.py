n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

s = []

def f():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(0, n):
        if s:
            if ls[i] in s:
                continue
            if ls[i] < s[-1]:
                continue
        s.append(ls[i])
        f()
        s.pop()

f()
            
            
