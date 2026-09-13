n = int(input())

list_of_names = []

for _ in range(n):
    name = input()
    list_of_names.append(name)

unique_names = set(list_of_names)

for name in unique_names:
    print(name)