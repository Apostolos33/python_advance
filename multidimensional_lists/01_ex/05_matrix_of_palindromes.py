r, c = map(int, input().split())

a = ord("a")


for row in range(r):
    for col in range(c):
        pass
        print(f"{chr(a + row)}{chr(a + row + col) }{chr(a + row)}", end=" ")
    print()