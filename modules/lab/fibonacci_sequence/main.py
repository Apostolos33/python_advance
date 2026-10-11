from modules.lab.fibonacci_sequence.core import create_sequence, locate
sequence = None

while True:
    command = input()
    if command == "Stop":
        break

    if command.split()[0] == "Create":
        sequence = create_sequence(int(command.split()[-1]))
        print(*sequence)
    else:
        if sequence:
            print(locate(sequence, int(command.split()[-1])))
        else:
            print("The sequence doesnt exist")