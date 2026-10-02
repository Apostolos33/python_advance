import os, re
from constants import path_to_dir

words_times_matched = {}

try:
    with open(os.path.join(path_to_dir, "file_handling", "lab", "text.txt")) as f:
        text = f.read()

    with open(os.path.join(path_to_dir, "files", "words.txt")) as f:
        words = f.read().split()

    for word in words:
        patern = rf"\b{word}\b"
        matched = re.findall(patern, text, re.IGNORECASE)
        words_times_matched[word] = len(matched)

    for word, times in sorted(words_times_matched.items(), key=lambda x: -x[1]):
        print(f"{word} - {times}")

except FileNotFoundError:
    print("file not found")