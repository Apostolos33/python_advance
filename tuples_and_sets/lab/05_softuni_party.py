number_of_guests = int(input())

reservation_numbers = set()

for _ in range(number_of_guests):
    reservation_numbers.add(input())

command = input()

while command != "END":
    if command in reservation_numbers:
        reservation_numbers.remove(command)
    command = input()

print(len(reservation_numbers))

for res in sorted(reservation_numbers):
    print(res)