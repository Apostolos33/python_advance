from collections import deque

water = int(input())

command = input()

people = deque()

while command != "Start":
    people.append(command)

    command = input()

command = input()

while command != "End":
    if command.isdigit():
        water_to_give = int(command)
        current_person = people.popleft()
        if water_to_give <= water:
            water -= water_to_give
            print(f"{current_person} got water")
        elif water_to_give > water:
            print(f"{current_person} must wait")
    elif command.startswith("refill "):
        liters = int(command.split()[1])
        water += liters

    command = input()

print(f"{water} liters left")