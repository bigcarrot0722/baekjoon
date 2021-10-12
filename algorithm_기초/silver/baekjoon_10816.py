int_plus = [0] * 10000001
int_minus = [0] * 10000001

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))
ans_list = []

for i in range(n):
    if n_list[i] >= 0:
        int_plus[n_list[i]] += 1
    else:
        int_minus[abs(n_list[i])] += 1

for i in range(m):
    if m_list[i] >= 0:
                  print(int_plus[m_list[i]], end = " ")
    else:
        print(int_minus[abs(m_list[i])], end = " ")
    
