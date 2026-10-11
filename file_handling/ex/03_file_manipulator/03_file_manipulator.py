import os

while True:
    command = input()
    if command == "End":
        break

    action, file, *arg = command.split("-")

    if action == "Create":
        open(file, "w").close()

    elif action == "Add":
        with open(file, "a") as f:
            f.write(f"{arg[0]}\n")

    elif action == "Replace":
        try:
            with open(file, "r+") as f:
                text = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(text.replace(arg[0], arg[1]))

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file)
        except FileNotFoundError:
            print("An error occurred")