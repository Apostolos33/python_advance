class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

valid_domains = ["com", "bg", "org", "net"]

email = input()

while email != "End":

    name = email.split("@")[0]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not "@" in email:
        raise MustContainAtSymbolError("Email must contain @")

    domain = email.split(".")[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()