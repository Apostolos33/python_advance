from collections import deque

kids = deque(input().split())

n = int(input())

while len(kids) > 1:
    kids.rotate(1 -n)
    kid_that_left = kids.popleft()
    print(f"Removed {kid_that_left}")

print(f"Last is {kids[0]}")