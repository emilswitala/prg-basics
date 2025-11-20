###
# ATM (cash machine) simulator
#
import time
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print('5. Change PIN')
    print("6. Exit ATM")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print(f'Checking PIN...')
        time.sleep(1)
        print(f'Your PIN is {pin}')
    elif choice == '5':
        y_n = input('Do you wish to change your PIN? (Y/N): ')
        if y_n == 'Y':
            confirm = input('Enter your new PIN: ')
            if confirm.isdigit == True:
                pin = confirm
            else:
                print('Invalid PIN. Try again')
        elif y_n == 'N':
            print("Okie bye!")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
