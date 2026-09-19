number_of_names = int(input())
current_row = 0
even_set = set()
odd_set = set()

for _ in range(number_of_names):
    name = input()
    current_row += 1
    sum_char_values = 0
    for char in name:
        value_of_char = ord(char)
        sum_char_values += value_of_char
    final_char_value = sum_char_values // current_row

    if final_char_value % 2 == 0:
        even_set.add(final_char_value)
    else:
        odd_set.add(final_char_value)

even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    print(*(even_set | odd_set), sep= ", ")
elif even_set_sum < odd_set_sum:
    print(*(odd_set - even_set), sep= ", ")
else:
    print(*(even_set ^ odd_set), sep= ", ")