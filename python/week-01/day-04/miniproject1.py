# ATM menu
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# use if elif else to perform selected operation

import random


name = input("Enter your name: ")
balance = 0
account_number = random.randint(100, 999)

print("=" * 35)
print(f"Welcome, {name}")
print(f"Account Number: {account_number}")
print("=" * 35)

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ₹{balance:.2f}\n")
    elif choice == "2":
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"₹{deposit_amount:.2f} deposited successfully.\n")
        else:
            print("Invalid deposit amount.")
    elif choice == "3":
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"₹{withdraw_amount:.2f} withdrawn successfully.\n")
        else:
            print("Invalid withdrawal amount or insufficient funds.\n")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

