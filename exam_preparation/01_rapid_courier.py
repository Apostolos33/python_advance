from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())

total_weight = 0

while couriers and packages:
    if couriers[0] >= packages[-1]:
        package_removed = packages.pop()
        total_weight += package_removed
        couriers_new_weight = couriers[0] - (package_removed * 2)
        couriers.popleft()

        if couriers_new_weight > 0:
            couriers.append(couriers_new_weight)
    else:
        total_weight += couriers[0]
        packages[-1] -= couriers[0]
        couriers.popleft()


print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if not packages and couriers:
    print(f"Couriers are still on duty: {', '.join([str(x) for x in couriers])} but there are no more packages to deliver.")

if  not couriers and packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join([str(x) for x in packages])}")