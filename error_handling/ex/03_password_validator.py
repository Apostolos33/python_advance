class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

special_characters = {"@", "*", "&", "%"}

def password_to_common(pwd, special):
    all_digit = pwd.isdigit()
    all_chars = pwd.isalpha()
    all_special = all(ch in special for ch in pwd)
    return all_digit or all_chars or all_special

while True:
    password = input()

    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_to_common(password, special_characters):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    for char in special_characters:
        if char in password:
            break
    else:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")