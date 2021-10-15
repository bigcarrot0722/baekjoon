a = input()

minus = a.split("-")

for i in range(len(minus)):
    if "+" in minus[i]:
        sum = 0
        plus = minus[i].split("+")
        for j in plus:
            sum += int(j)
        minus[i] = sum
    else:
        minus[i] = int(minus[i])


val = minus[0]
for i in range(1, len(minus)):
    val -= minus[i]

print(val)
