string_as_list = [char for char in input()]

characters_and_occurrences = {}

for char in string_as_list:
    if char not in characters_and_occurrences:
        characters_and_occurrences[char] = 0
    characters_and_occurrences[char] += 1

for character, occurrences in sorted(characters_and_occurrences.items()):
    print(f"{character}: {occurrences} time/s")