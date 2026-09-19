from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y > 0 else 0
    }

while nectar and working_bees:
    curr_nectar = nectar.pop()

    if curr_nectar >= working_bees[0]:
        curr_bee = working_bees.popleft()
        curr_symbol = symbols.popleft()
        result = abs(operators[curr_symbol](curr_bee, curr_nectar))
        honey += result

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")