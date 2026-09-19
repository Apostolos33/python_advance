first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}

n = int(input())

for _ in range(n):
    list_commands = input().split()
    command = list_commands[0] + " " + list_commands[1]
    numbers = [int(x) for x in list_commands[2:]]

    if command == "Add First":
        first_sequence.update(numbers)
    elif command == "Add Second":
        second_sequence.update(numbers)
    elif command == "Remove First":
        first_sequence.difference_update(numbers)
    elif command == "Remove Second":
        second_sequence.difference_update(numbers)
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(", ".join(str(x) for x in sorted(first_sequence)))
print(", ".join(str(x) for x in sorted(second_sequence)))