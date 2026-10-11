import os

files = {}

directory = "../"

# for element in os.listdir(directory):
#     f = os.path.join(directory, element)
#
#     if os.path.isfile(f):
#         ext = element.split(".")[-1]
#         if ext not in files:
#             files[ext] = []
#         files[ext].append(element)
#
#     elif os.path.isdir(f):
#         for el in os.listdir(f):
#             file_name = os.path.join(f, el)
#
#             if os.path.isfile(file_name):
#                 ext = el.split(".")[-1]
#                 if ext not in files:
#                     files[ext] = []
#                 files[ext].append(el)
#
# with open(os.path.join(directory, "report.txt"), "w") as output:
#     for ext, file_names in sorted(files.items()):
#         output.write(f".{ext}\n")
#         for file in sorted(file_names):
#             output.write(f"- - - {file}\n")



def get_files(folder, level= float("inf")):
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = element.split(".")[-1]
            if ext:
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)
        if os.path.isdir(f):
            get_files(f, level - 1)

get_files(directory, 2)

with open(os.path.join(directory, "report.txt"), "w") as output:
    for extension, file_names in sorted(files.items()):
        output.write(f".{extension}\n")
        for file in sorted(file_names):
            output.write(f"- - - {file}\n")



# for root, dirs, all_files in os.walk(directory):
#     for file in all_files:
#         ext = file.split(".")[-1]
#         if ext:
#             if ext not in files:
#                 files[ext] = []
#             files[ext].append(file)
#
# with open(os.path.join(directory, "report.txt"), "w") as output:
#     for extension, file_names in sorted(files.items()):
#         output.write(f".{extension}\n")
#         for file in sorted(file_names):
#             output.write(f"- - - {file}\n")