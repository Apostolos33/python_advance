numbers = tuple(map(float, input().split()))

numbers_and_accuracies = {}

for number in numbers:
    if number not in numbers_and_accuracies:
        numbers_and_accuracies[number] = 0
    numbers_and_accuracies[number] += 1

for key, value in numbers_and_accuracies.items():
    print(f"{key} - {value} times")