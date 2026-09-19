first_set_length, second_set_length = [ int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(first_set_length):
    first_set.add(input())

for _ in range(second_set_length):
    second_set.add(input())
intersection = first_set.intersection(second_set)

for section in intersection:
    print(section)