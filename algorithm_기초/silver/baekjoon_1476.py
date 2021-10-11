e, s, m = map(int, input().split())

year = 1
e_year = 1
s_year = 1
m_year = 1
while True:
    e_year = year % 15
    if e_year == 0:
        e_year = 15
    s_year = year % 28
    if s_year == 0:
        s_year = 28
    m_year = year % 19
    if m_year == 0:
        m_year = 19
    if e_year == e and s_year == s and m_year == m:
        print(year)
        break
    year += 1
