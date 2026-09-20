from collections import deque

r, c = [int(x) for x in input().split()]
string = deque(input())

for row in range(r):
    current_row = []
    for col in range(c):
        current_row.append(string[0])
        string.rotate(-1)

    if row % 2 != 0:
        current_row.reverse()

    print("".join(current_row))