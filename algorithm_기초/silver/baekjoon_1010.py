def bridge(west, east):
    key_mul = east
    key_div  = west
    sum = 1
    for i in range(west):
        sum *= key_mul
        key_mul -= 1
    for i in range(west):
        sum //= key_div
        key_div -=1
    return sum
for _ in range(int(input())):
    west, east = map(int,input().split())
    print(bridge(west, east))
