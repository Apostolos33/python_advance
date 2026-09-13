box_of_clothes = [int(x) for x in input().split()]

capacity_per_rack = int(input())
racks_used = 0

while box_of_clothes:
    rack = capacity_per_rack
    while rack > 0:
        if box_of_clothes:
            if box_of_clothes[-1] <= rack:
                rack -= box_of_clothes.pop()
            else:
                break
        else:
            break
    racks_used += 1

print(racks_used)