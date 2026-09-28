#Variables for Bank system
Bank = 0
HaveAccount = 0
AccountBalance = 0
Deposit = 0
PIN = 0
PINC =0

#Variables for Username and Password
UN = 0
PW = 0
User = UN
Pass = PW


print("===============Welcome to KingKhalidUniversity Bank===============")
print("")
print("First you have to create account.")

while HaveAccount == 0:
    print("===============KKU Bank create account===============")
    print("")
    print("Please enter the required information.")

    # Validate ZIP
    while True:
        ZIP = input("Enter your ZIP code number: ")
        if ZIP.isdigit():
            break
        else:
            print("")
            print("Please enter correct ZIP code.")

    # Validate University ID
    while True:
        ID = input("Enter your university ID: ")
        if ID.isdigit():
            break
        else:
            print("")
            print("Please enter correct university ID.")

    # Validate Phone Number
    while True:
        PhoneNum = input("Enter your phone number: ")
        if PhoneNum.isdigit():
            break
        else:
            print("")
            print("Please enter correct phone number.")

    # Validate email
    while True:
        email = input("Enter your university email: ")
        if email.startswith("447") and email.endswith("@kku.edu.sa"):
            break
        else:
            print("")
            print("Please enter correct email.")

    # Get Username and Password
    UN = input("Enter your new username: ")
    PW = input("Enter your new password: ")

    # Validate PIN with confirmation
    while True:
        PIN = input("Enter your new PIN: ")
        PINC = input("Confirm your new PIN: ")

        if PINC == PIN:
            print("")
            print("=================KingKhalidUniversity Bank===============")
            print("Account created successfully!")
            break
        else:
            print("")
            print("=================KingKhalidUniversity Bank===============")
            print("PIN is incorrect. Please try again.")

    # Ask if user has account
    while True:
        try:
            HaveAccount = int(input("Do you have an account?    1=Yes 0=No: "))
            if HaveAccount == 1 or HaveAccount == 0:
                break
            else:
                print("")
                print("===============KingKhalidUniversity Bank===============")
                print("Invalid input. Please try again.")
        except ValueError:
            print("")
            print("===============KingKhalidUniversity Bank===============")
            print("Invalid input. Please enter 0 or 1.")

if HaveAccount == 1:
    print("")
    print("===============KingKhalidUniversity Bank===============")
    User = input("Enter your username: ")
    Pass = input("Enter your password: ")
    PINU = input("Enter your PIN: ")

while User != UN and Pass != PW or PINU != PIN:
    print("")
    print("===============KingKhalidUniversity Bank===============")
    print("Invalid, username or password or PIN is incorrect. Please try again.")
    User = input("Enter your username: ")
    Pass = input("Enter your password: ")
    PINU = input("Enter your PIN: ")


while User == UN and Pass == PW and PINU == PIN:
    print("")
    print("===============KingKhalidUniversity Bank===============")

    while True:
        try:
            Bank = int(input("Please choose Withdrawal =1 or Deposit =2: "))
            if Bank == 1 or Bank == 2:
                break
            else:
                print("")
                print("===============KingKhalidUniversity Bank===============")
                print("Invalid input. Please try again.")
        except ValueError:
            print("")
            print("===============KingKhalidUniversity Bank===============")
            print("Invalid input. Please enter 1 or 2.")

    if Bank == 2:
        print("")
        print("===============KKU Bank Deposit===============")
        Deposit = input("Enter your deposit amount 1-5000: ")

        # Check if input is a valid number
        if Deposit.isdigit():
            Deposit = int(Deposit)  # Convert to integer

            if Deposit > 5000:
                print("")
                print("===============KKU Bank Deposit===============")
                print("Invalid, Deposit amount is greater than 5000. Please try again.")

            elif Deposit < 1:
                print("")
                print("===============KKU Bank Deposit===============")
                print("Invalid, Deposit amount must be at least 1. Please try again.")

            else:
                print(f"This is the amount that you deposit {Deposit}$")
                AccountBalance = AccountBalance + Deposit
                print(f"Account balance {AccountBalance}$")

        else:
            print("")
            print("===============KKU Bank Deposit===============")
            print("Invalid input. Please enter a number.")

    elif Bank == 1:
        print("")
        print("===============KKU Bank Withdrawal===============")
        Withdrawal = input("Enter your withdrawal amount: ")

        # Check if input is a valid number
        if Withdrawal.isdigit():
            Withdrawal = int(Withdrawal)  # Convert to integer

            if Withdrawal > AccountBalance:
                print("")
                print("===============KKU Bank Withdrawal===============")
                print("Invalid, Withdrawal amount is greater than Account balance. Please try again.")

            elif Withdrawal < 1:
                print("")
                print("===============KKU Bank Withdrawal===============")
                print("Invalid, Withdrawal amount must be at least 1. Please try again.")

            else:
                print(f"This is the amount that you withdrawal {Withdrawal}$")
                AccountBalance = AccountBalance - Withdrawal
                print(f"Account balance {AccountBalance}$")

        else:
            print("")
            print("===============KKU Bank Withdrawal===============")
            print("Invalid input. Please enter a number.")

