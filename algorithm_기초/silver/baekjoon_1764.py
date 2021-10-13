n, m = map(int, input().split())
n_list = []
m_list = []

for i in range(n):
    n_list.append(input())

for j in range(m):
    m_list.append(input())

n_list = set(n_list)
m_list = set(m_list)

n_and_m = n_list & m_list
n_and_m = list(n_and_m)
n_and_m.sort()
print(len(n_and_m))
for i in n_and_m:
    print(i)
