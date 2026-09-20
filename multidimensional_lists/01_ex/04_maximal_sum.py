rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sub_matrix = []
biggest_sum = float("-inf")

for r in range(rows -2):
    for c in range(cols -2):
        first_num = matrix[r][c]
        right_num = matrix[r][c+1]
        right_right_num = matrix[r][c+2]
        down_num = matrix[r+1][c]
        down_right_num = matrix[r + 1][c + 1]
        last_down_num = matrix[r + 1][c + 2]
        down_down_num = matrix[r+2][c]
        down_down_right_num = matrix[r+2][c+1]
        down_right_right_num = matrix[r+2][c+2]
        sum_numbers = first_num + right_num + right_right_num + down_num + down_right_num + last_down_num + down_down_num + down_down_right_num + down_right_right_num
        if sum_numbers > biggest_sum:
            biggest_sum = sum_numbers
            sub_matrix = [[first_num, right_num, right_right_num], [down_num, down_right_num, last_down_num], [down_down_num, down_down_right_num, down_right_right_num]]

print(f"Sum = {biggest_sum}")
for nums in sub_matrix:
    print(*nums)