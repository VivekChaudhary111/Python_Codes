class Bank:
    def __init__(self, account_num, account_holder, balance =0 ):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

class SavingAccount(Bank):
    def __init__(self, account_num, account_holder, balance =0, interest_rate = 0.2):
        self.interest_rate = interest_rate
        super().__init__(account_num, account_holder, balance)

    def add_interest(self):
        amount = self.balance * self.interest_rate
        self.balance += amount

class CheckingAccount(Bank):
    def __init__(self, account_num, account_holder, overlimit_draft = 100):
        super().__init__(account_num, account_holder, balance)
        self.overlimit_draft = overlimit_draft

    def withdraw(self, amount):
        if amount <= self + self.overlimit_draft:
            self.balance -= amount
        else:
            print("Insufficient Balance!")
accounts = []
count = 0
while 1:
    print('''
Welcome to GLA Bank
which account you want to open
    1. Saving Account
    2. Checking Account
    3. Current Account
    4. Exit
''')
    choice = int(input('Enter the choice 1/2/3 '))
    if choice == 1:
        ac = SavingAccount(10000001, 'Ravi', 100)
        accounts.append(ac)

        while 1:
            print('Menu')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Exit')
        ch = int(input('Enter the choice 1/2/3 '))
        if ch == 1:
            accounts[count].Deposit(1000)


        count+=1
    elif choice == 4:
        break




if __name__ == "__main__":
    saving_account1 = SavingAccount(1230099, 'Ravi', 100)
    checking_account1 = CheckingAccount(113133, 'Saket', 1200)
