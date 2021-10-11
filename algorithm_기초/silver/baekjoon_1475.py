num = input()
ls  = [0] * 10
for i in range(10):
    ls[i] = num.count(str(i))

six = ls[6]
ls[6] = 0
nine = ls[9]
ls[9] = 0
if max(ls) < round((six + nine)/2):
    print(round((six + nine)/2))
else:
    print(max(ls))

