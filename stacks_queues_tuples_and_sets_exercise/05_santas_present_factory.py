from collections import deque

materials = [int(x) for x in input().split()]

magic = deque([int(x) for x in input().split()])

presents = {
    "150": "Doll",
    "250": "Wooden train",
    "300": "Teddy bear",
    "400": "Bicycle"
}

crafted_presents = {}

while materials and magic:
    curr_magic = magic[0]
    curr_material = materials[-1]
    result = curr_magic * curr_material
    if magic[0] == 0 or materials[-1] == 0:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()
        continue

    if result < 0:
        curr_result = curr_magic + curr_material
        magic.popleft()
        materials.pop()
        materials.append(curr_result)

    else:
        if str(result) not in presents:
            magic.popleft()
            materials[-1] += 15
        else:
            if presents[str(result)] not in crafted_presents:
                crafted_presents[presents[str(result)]] = 0
            crafted_presents[presents[str(result)]] += 1

            magic.popleft()
            materials.pop()

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

if crafted_presents:
    for key, value in sorted(crafted_presents.items()):
        print(f"{key}: {value}")