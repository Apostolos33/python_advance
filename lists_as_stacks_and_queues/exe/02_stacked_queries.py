n = int(input())

stack = []

for _ in range(n):
    queries = input().split()

    if queries[0] == "1":
        stack.append(int(queries[1]))
    elif queries[0] == "2":
        if stack:
            stack.pop()
    elif queries[0] == "3":
        if stack:
            print(max(stack))
    elif queries[0] == "4":
        if stack:
            print(min(stack))

print(*(str(x) for x in reversed(stack)), sep=", ")