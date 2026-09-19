number_of_intersections = int(input())

longest_intersection = 0
longest_intersection_set = set()

for _ in range(number_of_intersections):
    first_set = set()
    second_set = set()
    first, second = input().split("-")
    first_start, first_end = map(int, first.split(","))
    second_start, second_end = map(int, second.split(","))
    for i in range(first_start, first_end + 1):
        first_set.add(i)
    for i in range(second_start, second_end + 1):
        second_set.add(i)
    intersection = first_set.intersection(second_set)
    if len(intersection) > longest_intersection:
        longest_intersection = len(intersection)
        longest_intersection_set = intersection

print(f"Longest intersection is {list(longest_intersection_set)} with length {longest_intersection}")