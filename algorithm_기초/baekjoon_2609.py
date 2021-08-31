def factor(num):
    a = 2
    fac = []
    while a <= num:
        if num % a == 0:
            fac.append(a)
            num = num // a
        else:
            a += 1
    return fac

A = []
B = []

min = 1
max = 1

a, b = map(int, input().split())

A = factor(a)
B = factor(b)

for i in A:
    if i in B:
        min *= i
        max *= i
        B.remove(i)
    else:
        max *= i

for i in B:
    max *= i

print(min,max)
