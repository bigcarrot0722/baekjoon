from collections import deque

deq = deque()

a, b = map(int, input().split())
b -= 1

for i in range(1, a + 1):
    deq.append(i)

print("<",end="")
while len(deq) != 1:
    deq.rotate(-b)
    print(deq.popleft(),end=", ")
print(deq[0],end="")
print(">",end="")
