import os
from constants import path_to_dir

path = os.path.join(path_to_dir, "files", "numbers.txt")

try:
    with open(path) as f:
        numbers = [int(x) for x in f]
        print(sum(numbers))
except FileNotFoundError:
    print("file not found")