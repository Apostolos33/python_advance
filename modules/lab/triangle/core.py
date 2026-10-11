def print_triangle(number):
    for row in range(1, number + 2):
        for col in range(1, row):
            print(col, end= " ")
        print()
    for row in range(number, 1, -1):
        for col in range(1, row):
            print(col, end= " ")
        print()