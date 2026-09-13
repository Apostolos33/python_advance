from collections import deque

food = int(input())

orders = deque(map(int, input().split()))

print(max(orders))

while food > 0:
    if orders:
        if orders[0] <= food:
            food -= orders.popleft()
        else:
            break
    else:
        break

if not orders:
    print("Orders complete")
else:
    print("Orders left:", *orders)
