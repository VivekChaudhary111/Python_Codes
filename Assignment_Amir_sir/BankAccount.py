import random
import itertools

class BankAccount:

    Used_account_numbers =[]
    id_iter = itertools.count(1)

    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.Account_balance = 0.0
        self.transactions = []
        self.id = next(BankAccount.id_iter)

        while True:
            value=random.randint(3000000000, 4000000000)
            if value not in BankAccount.Used_account_numbers:
                self.Account_number = value
                BankAccount.Used_account_numbers.append(self.Account_number)
                break
            
    def display_account_details(self):
        print(f'''
Name: {self.name}
Address:{self.address}
Account No.: {self.Account_number}
Id: {self.id}

''')

    def deposit_money(self, deposit_amount):
        self.Account_balance += deposit_amount
        self.transactions.append(f'Rs. {deposit_amount:.2f} deposited successfully.')
        print(f'\nRs. {deposit_amount:.2f} deposited successfully.')

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount <= self.Account_balance:
            self.Account_balance -= withdraw_amount
            self.transactions.append(f'Rs. {withdraw_amount:.2f} withdrawn successfully.')
            print(f'\nRs. {withdraw_amount:.2f} withdrawn successfully.')
        else:
            self.transactions.append(f"Rs. {withdraw_amount:.2f} Transaction Failed! Insufficient Account Balance.")
            print(f"\nRs. {withdraw_amount:.2f} Transaction Failed! Insufficient Account Balance.")

    def check_balance(self):
        print(f"\nYour account_dict[name] balance is Rs. {self.Account_balance:.2f}")
    
    def set_pin(self, pin):
        self.pin = pin
        print(f'\nPIN has saved successfully.')
    
    def update_pin(self, update_pin):
        self.pin = update_pin
        print(f'\nPIN has updated successfully.')


#Main code

account_dict = {}  # Dictionary to store account_dict[name] objects
count = 0
while True:
    print('\nBank Management Menu')
    print('''
1. Open Bank Account.
2. Deposit Money.
3. Withdraw Money.
4. Check Balance.
5. PIN related.
6. Display Account Details.
7. Display all Transactions.
8. Exit.
          
''')
    
    choice = int(input("Enter Your choice[1-8]: "))
    if choice == 1:
        print("Enter your details below")
        name = input("Enter your Name: ")
        address = input("Enter your Address: ")

        account_dict[name] = BankAccount(name, address)  # Create new account_dict[name] object
        print('\nYour account has opened successfully.')

        account_dict[name] = account_dict[name]  # Store the account_dict[name] object in the dictionary
        count += 1
        account_dict[name].display_account_details()
        print(account_dict)
    elif choice == 2:
        name = input("Enter your Name: ")  # Get the name of the account holder
        deposit_amount = int(input("Enter the amount to deposit: "))
        try:
            account_dict[name].deposit_money(deposit_amount)
        except:
            print("\nPlease! First open the account.")
            continue

    elif choice == 3:
        name = input("Enter your Name: ")  # Get the name of the account holder
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        pin = int(input("Enter the PIN: "))
        try:
            if account_dict[name].pin:
                if pin == account_dict[name].pin:
                    account_dict[name].withdraw_money(withdraw_amount)
                else:
                    print("\nPIN do not match\nTry again later.")
                    continue
        except:
            print('\nPlease set the PIN first, then try again.')
            continue

    elif choice == 4:
        name = input("Enter your Name: ")  # Get the name of the account holder
        pin = int(input("Enter the PIN: "))
        try:
            if account_dict[name].pin:
                if pin == account_dict[name].pin:
                    account_dict[name].check_balance()
                else:
                    print("\nPIN do not match\nTry again later.")
                    continue
        except:
            print('\nPlease set the PIN first, then try again.')
            continue

    elif choice == 5:
        while True:
            print('''
1. Set PIN.
2. Update PIN.
3. Forgot PIN.
4. Main menu.

''')
            ch = int(input("Enter the choice[1-4]: "))
            if ch == 1:
                try:
                    name = input("Enter your Name: ")  # Get the name of the account holder
                    if account_dict[name].pin:
                        print("\nYou have already added the PIN.")
                        continue
                except:
                    set_pin = int(input("Enter the new PIN: "))
                    account_dict[name].set_pin(set_pin)
            
            elif ch == 2:
                try:
                    name = input("Enter your Name: ")  # Get the name of the account holder
                    if account_dict[name].pin:
                        old_pin = int(input("Enter the old PIN: "))
                        if old_pin == account_dict[name].pin:
                            new_pin = int(input("Enter the new PIN: "))
                            account_dict[name].update_pin(new_pin)
                        else:
                            print("\nPIN do not match\nTry again later.")
                            continue      
                except:
                    print("\nYou have to set the new PIN.")
                    continue
            
            elif ch == 3:
                try:
                    name = input("Enter your Name: ")
                    address = input("Enter your Address: ")
                    ac_no = int(input("Enter your account number: "))
                    if name == account_dict[name].name and address == account_dict[name].address and ac_no == account_dict[name].Account_number:
                        set_pin = int(input("Enter the new PIN: "))
                        account_dict[name].set_pin(set_pin)
                    else:
                        print("\nDetails do not match\nTry again later.")
                except:
                    print("\nPlease! First open the account.")
                    continue

            elif ch == 4:
                break

    elif choice == 6:
        try:
            name = input("Enter your Name: ")  # Get the name of the account holder
            account_dict[name].display_account_details()
        except:
            print("\nPlease! First open the account.")
            continue
    
    elif choice == 7:
        try:
            name = input("Enter your Name: ")  # Get the name of the account holder
            print("\nTransaction history...from old to latest")
            for i in account_dict[name].transactions:
                print(i)
        except:
            print("\nPlease! First open the account.")
            continue

    elif choice == 8:
        print("\nThanks for choosing us. Have a nice day!")
        break
    