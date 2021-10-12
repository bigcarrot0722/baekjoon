from collections import deque
n = int(input())
card = deque([i for i in range(1, n + 1)])

while len(card) != 1:
    card.popleft()
    insert_bottom = card.popleft()
    card.append(insert_bottom)

print(card[0])

        
