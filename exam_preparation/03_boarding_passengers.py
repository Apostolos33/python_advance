def boarding_passengers(initial_capacity, *args):
    capacity = initial_capacity
    passengers_boarded = 0
    passengers_needed_to_be_boarded = 0
    plans_and_passengers = {}
    result = ""

    for arg in args:
        passengers_needed_to_be_boarded += arg[0]

    for arg in args:

        if arg[0] <= capacity:
            if not arg[1] in plans_and_passengers:
                plans_and_passengers[arg[1]] = 0
            plans_and_passengers[arg[1]] += arg[0]
            capacity -= arg[0]
            passengers_boarded += arg[0]
        else:
            continue

    result += "Boarding details by benefit plan:\n"
    sorted_plans_and_passengers = sorted(plans_and_passengers.items(), key=lambda x: (-x[1], x[0]))

    for plan, passengers in sorted_plans_and_passengers:
        result += f"## {plan}: {passengers} guests\n"

    if passengers_boarded == passengers_needed_to_be_boarded:
        result += "All passengers are successfully boarded!"
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))