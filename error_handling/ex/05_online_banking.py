class MoneyNotEnoughError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

class PINCodeError(Exception):
    pass

pin_code, balance, age = map(int, input().split(", "))

while True:
    command = input()

    if command == "End":
        break

    command_as_list = command.split("#")

    if command_as_list[0] == "Send Money":
        money_to_send, pin_entered = int(command_as_list[1]), int(command_as_list[2])

        if money_to_send > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin_entered != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money_to_send
        print(f"Successfully sent {money_to_send:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")
    elif command_as_list[0] == "Receive Money":
        money_to_receive = int(command_as_list[1])

        if money_to_receive < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += money_to_receive / 2
        print(f"{money_to_receive / 2:.2f} money went straight into the bank account")