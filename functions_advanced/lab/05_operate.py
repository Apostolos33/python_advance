from functools import reduce
def sum_numbers(*args):
    return sum(args)

def sub_numbers(*args):
    return reduce(lambda x, y: x - y, args)

def mul_numbers(*args):
    return reduce(lambda x, y: x * y, args)

def divide_numbers(*args):
    return reduce(lambda x, y: x / y, args)

mapper = {
    "+": sum_numbers,
    "-": sub_numbers,
    "*": mul_numbers,
    "/": divide_numbers
}

def operate(operator: str, *args) -> int:
    function = mapper.get(operator)
    return function(*args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))