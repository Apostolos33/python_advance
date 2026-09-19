from collections import deque

robots_raw = input().split(';')
starting_time = input()
hours, minutes, seconds = map(int, starting_time.split(':'))
curr_time = hours * 3600 + minutes * 60 + seconds

robots = []
for r in robots_raw:
    name, time_str = r.split('-')
    robots.append({
        "name": name,
        "time": int(time_str),
        "busy_until": 0
    })

products = deque()
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    curr_time += 1
    curr_product = products.popleft()

    assigned = False
    for robot in robots:
        if robot["busy_until"] <= curr_time:
            robot["busy_until"] = curr_time + robot["time"]

            h = (curr_time // 3600) % 24
            m = (curr_time % 3600) // 60
            s = curr_time % 60

            print(f'{robot["name"]} - {curr_product} [{h:02d}:{m:02d}:{s:02d}]')
            assigned = True
            break

    if not assigned:
        products.append(curr_product)