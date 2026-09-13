from collections import deque

people = deque()

while True:
    command = input()
    if command == "End":
        break

    elif command == "Paid":
        for _ in range(len(people)):
            paid_customer = people.popleft()
            print(paid_customer)
    else:
        people.append(command)

print(f"{len(people)} people remaining.")