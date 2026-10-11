from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def is_not_valid_user_data(**user):
    if user["username"] == "" or user["password"] == "" or user["first_name"] == "" or user["last_name"] == "":
        return "All fields are required!"


    if len(user["username"]) < 4:
        return "Username must be at least 4 characters long"

    if len(user["password"]) < 4:
        return "Password must be at least 4 characters long"

    pass_validation_map = {"upper": False, "lower": False, "digit": False, "special": False}

    for ch in user["password"]:
        if ch in ascii_uppercase:
            pass_validation_map["upper"] = True
        elif ch in ascii_lowercase:
            pass_validation_map["lower"] = True
        elif ch in digits:
            pass_validation_map["digit"] = True
        elif ch in punctuation:
            pass_validation_map["special"] = True

    if not all(pass_validation_map.values()):
        return "Password must contain at least 1 special character, 1 upper case letter, 1 digit, 1 lower case letter "

    if len(user["first_name"]) < 2:
        return "First name must be least two characters long"

    if len(user["last_name"]) < 2:
        return "Last name must be least two characters long"
    return None