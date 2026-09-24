n_presents = int(input())
n = int(input())

matrix = []
s_r, s_c = 0, 0
good_kids = 0
happy_good_kids = 0

for row in range(n):
    curr_row = input().split()
    if "S" in curr_row:
        s_r = row
        s_c = curr_row.index("S")
    matrix.append(curr_row)
    for ch in curr_row:
        if ch == "V":
            good_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while n_presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    d_r = directions[command][0]
    d_c = directions[command][1]
    n_r = s_r + d_r
    n_c = s_c + d_c
    if 0 <= n_r < n and 0 <= n_c < n:
        matrix[s_r][s_c] = "-"
        if matrix[n_r][n_c] == "V":
            good_kids -= 1
            happy_good_kids += 1
            n_presents -= 1
        elif matrix[n_r][n_c] == "C":
            for c_r, c_c in directions.values():
                if n_presents == 0:
                    break
                sc_r = n_r + c_r
                sc_c = n_c + c_c
                if 0 <= sc_r < n and 0 <= sc_c < n:
                    if matrix[sc_r][sc_c] == "X":
                        n_presents -= 1
                    elif matrix[sc_r][sc_c] == "V":
                        n_presents -= 1
                        good_kids -= 1
                        happy_good_kids += 1

                    matrix[sc_r][sc_c] = "-"


        matrix[n_r][n_c] = "S"
        matrix[s_r][s_c] = "-"
        s_r, s_c = n_r, n_c

if n_presents < 1 and good_kids > 0:
    print("Santa ran out of presents!")
for m_row in matrix:
    print(' '.join(m_row))
if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {happy_good_kids} happy nice kid/s.")