from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
    for row, line in enumerate(input_file, start=1):
        letters = 0
        punctuation_marks = 0
        for char in line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                punctuation_marks += 1

        output_file.write(f"Line {row}: {line.strip()} ({letters})({punctuation_marks})\n")