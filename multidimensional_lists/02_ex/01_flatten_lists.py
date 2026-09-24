first_list = input().split("|")

matrix = []

for i in range(len(first_list) - 1, -1, -1):
    if first_list[i]:
        matrix.append(first_list[i].split())

for ls in matrix:
    if ls:
        print(' '.join(ls), end=" ")