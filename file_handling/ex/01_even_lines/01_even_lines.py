symbols = {"-", ",", ".", "!", "?"}

with open("text.txt") as f:
    for row, line in enumerate(f):
        if row % 2 == 0:
            for char in symbols:
               line = line.replace(char, "@")
            print(*reversed(line.split()))
