def show_initalmenu():
    print()
    print("Welcome to Terminal Teller!:")
    print()
    print("1) create account")
    print("2) log in")
    print("3) quit")

def get_FirstName():
    return input("First name: ")

def get_LastName():
    return input("Last name: ")

def get_pin():
    return input(" PIN: ")

def get_confirmpin():
    return input("confirm PIN: ")


def show_mainmenu(clientname,account_number):
    print()
    print("Hello, {}({})".format(clientname,account_number))
    print()
    print("1) Check balance")
    print("2) Withdraw funds")
    print("3) Deposit fund")
    print("4) sign out")



def get_input():
    print()
    print("Your choice: ", end="")
    return input()
    # same as return input("Your choice: ")

def bad_input():
    print("Invalid input")

def get_deposit():
    print()
    print("How much to deposit: ", end="")
    return input()

def accountcheck():
    print()
    print("Account Number: ", end="")
    return input()

def clientcheck():
    print()
    print("Client: ", end="")
    return input()


def pincheck():
    print()
    print("Pin ", end="")
    return input()

def get_withdraw():
    print()
    print("How much to withdraw: ", end="")
    return input()

def insufficient_fund(B):
    if B<0:
        print("INSUFFICIENT FUND!!!")

def goodby():
    print("GOODBYE!")

def show_balance(balance):
    print()
    print("Your Balance is  {}.".format(balance))




