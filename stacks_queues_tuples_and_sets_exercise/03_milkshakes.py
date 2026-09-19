from collections import deque

chocolates = [int(x) for x in input().split(", ")]

cups_of_milks = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milks:
    curr_cup = cups_of_milks[0]
    curr_chocolate = chocolates[-1]
    if curr_cup <= 0 or curr_chocolate <= 0:
        if curr_cup <= 0:
            cups_of_milks.popleft()
        if curr_chocolate <= 0:
            chocolates.pop()
        continue

    if curr_chocolate == curr_cup:
        milkshakes += 1
        cups_of_milks.popleft()
        chocolates.pop()

    else:
        cups_of_milks.rotate(-1)
        chocolates[-1] -= 5

print(f"{'Great! You made all the chocolate milkshakes needed!' if milkshakes == 5 else 'Not enough milkshakes.'}")
print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, cups_of_milks)) if cups_of_milks else 'empty'}")