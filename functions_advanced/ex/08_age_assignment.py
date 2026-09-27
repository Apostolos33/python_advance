def age_assignment(*args, **kwargs):
    new_dict = {}
    result = []
    for name in args:
        new_dict[name] = kwargs[name[0]]
    for name, age in sorted(new_dict.items()):
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))