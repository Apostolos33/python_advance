def create_matrix_take_bee_position(number):
    matr = []
    bee_c = 0
    bee_r = 0
    for num in range(number):
        row = [x for x in input()]
        if "B" in row:
            bee_c = row.index("B")
            bee_r = num
        matr.append(row)
    return matr, bee_r, bee_c

def move_bee(comm, ma, mape, be_r, be_c):
    m_r, m_c = mape[comm]
    n_r = be_r + m_r
    n_c = be_c + m_c

    if 0 > n_r:
        n_r = len(ma) - 1
    elif n_r >= len(ma):
        n_r = 0
    if n_c < 0:
        n_c = len(ma) - 1
    elif n_c >= len(ma):
        n_c = 0

    return n_r, n_c

def print_matrix(ma):
    for row in ma:
        print("".join(row))


n = int(input())

matrix, b_r, b_c = create_matrix_take_bee_position(n)

second_chance = 1
reached_hive = False
bees_energy = 15
nectar_collected = 0

mapper = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while True:
    command = input()
    bees_energy -= 1



    matrix[b_r][b_c] = "-"
    b_r, b_c = move_bee(command, matrix, mapper, b_r, b_c)

    if matrix[b_r][b_c] == "H":
        matrix[b_r][b_c] = "B"
        reached_hive = True
        break
    if matrix[b_r][b_c].isdigit():
        nectar_collected += int(matrix[b_r][b_c])

    matrix[b_r][b_c] = "B"

    if bees_energy == 0:
        if nectar_collected >= 30 and second_chance:
            restored = nectar_collected - 30
            nectar_collected = 30
            second_chance = 0

            if restored > 0:
                bees_energy = restored
            else:
                print("This is the end! Beesy ran out of energy.")
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            break


if reached_hive and nectar_collected >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {bees_energy}")
elif reached_hive:
    print("Beesy did not manage to collect enough nectar.")

print_matrix(matrix)