number_of_elements = int(input())

unique_elements = set()

for _ in range(number_of_elements):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

for unique_element in unique_elements:
    print(unique_element)