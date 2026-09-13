from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    curr_fuel, curr_dist = input().split()
    pumps.append({"fuel": int(curr_fuel), "dist": int(curr_dist)})

start_position = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    stops = 0
    for i in range(pumps_num):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["dist"]

        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break

        fuel -= distance
        stops += 1

print(start_position)