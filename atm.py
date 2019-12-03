#name: Gabrielle Gervasi
#email: Gabrielle.Gervasi1@marist.edu
#description: ATM, withdrawl, deposit, ext.
#This is impossible


class ATM:
    def __init__(self, filename):
        self.filename= filename
        self.load_customers()
        filename= 'accounts.txt'
        text= open(filename, 'r').read()
        self.id_pin_dict={}
        for cust in self.cust_list:
            self.id_pin_dict[tuple(cust.get_id())] = cust.get_pin()
    
            self.cust= self.login()
            self.menu()

    def login(self):
        uid= input('Enter your user id: ')
        pin= input('Enter your pin: ')
        text= open("accounts.txt", 'r')
        if (uid, pin) not in self.id_pin_dict.items():
            print('\nInvalid id or pin.')
            uid=input('Enter your user id: ' )
            pin = input('Enter your pin: ')
        return [cust for cust in self.cust_list if cust.get_id() == uid]
    

    def menu(self):
        print('\nMenu\n' +
              '(1) See Balance\n' +
              '(2) Withdraw funds\n' +
              '(3) Deposit funds\n' +
              '(4) Transfer funds')
        choice = eval(input('Select 1-4: '))
        [self.get_balance, self.withdraw, self.deposit, self.transfer][choice-1]()

    def get_balance(self):
        acct= input('\nChecking (c) or savings (s) account: ')
        if acct[0].lower() == 'c':
            print('Checking Balance:', self.cust.get_cbal())
        else:
            print('Savings Balance:', self.cust.get_sbal())
        self.again()
        
    def withdraw(self):
        acct= input('\nChecking (c) or savings (s) account: ')
        amt= eval(input('How much would you like to withdraw? '))
        if acct == 'c':
            if 0<= amt <= self.cust.get_cbal():
                self.cust.withdraw(amt, 'c')
                print('New Checking Balance:', self.cust.get_cbal())
            elif amt<0:
                print ('Nope. You can\'t withdraw negative funds.')
            else:
                print('Insufficient funds')
        else:
            if 0 <= amt <= self.cust.get_sbal():
                self.cust.withdraw(amt, 's')
                print('New Savings Balance:', self.cust.get_sbal())
            elif amt < 0:
                print ('Nope. You can\'t withdraw negative funds.')
            else:
                print('Insufficient funds')
        self.again()

    def deposit(self):
        acct= input('\nChecking (c) or savings (s) account: ')
        amt= eval(input('How much would you like to deposit? '))
        if acct == 'c':
            self.cust.deposit (amt, 'c')
            print('New Checking Balance:', self.cust.get_cbal())
        else:
            self.cust.deposit(amt, 's')
            print('New Savings Balance:', self.cust.get_sbal())
        self.again()

    def transfer(self):
        tfr = input('\nChecking to savings (cts) or savings to checking (stc)?')
        amt = eval(input('Amount to transfer: '))
        if tfr == 'cts':
            if 0 <= amt <= cust.get_cbal():
                self.cust.withdraw(amt, 'c')
                print('New Checking Balance:', self.cust.get_cbal())
                self.cust.deposit(amt, 's')
                print('New Savings Balance:', self.cust.get_sbal())
            elif amt < 0:
                print('Nope. You can\'t withdraw negative funds.')
            else:
                print('Insuffiencient funds')
        else:
            if 0 <= amt <= self.cust.get_sbal():
                self.cust.withdraw(amt, 's')
                print('New Savings Balance: ', self.cust.get_sbal())
                self.cust.deposit(amt, 'c')
                print('New Checking Balance:', self.cust.get_cbal())
            elif amt < 0:
                print('Nope. You cant\'t withdraw negaitve funds.')
            else:
                print('Insuffiecient funds')

    def again(self):
        y_or_n= input('\nWould you like to make another transaction? ')
        if y_or_n[0].lower() == 'y':
            self.menu()
        else:
            self.close()

    def close(self):
        print('Bye')
        self.save_customers()

    def load_customers(self):
        try:
            fileObj = open(self.filename, 'r')
        except FileNotFoundError:
            fileObj = open(self.filename, 'w')
            filename.close()
            fileObj = open(self.filename, 'r')
        self.cust_list = []
        for line in fileObj:
            uid= line.split("\t")
            pin= line.split("\t")
            cb= line.split("\t")
            sb= line.split("\t")
            self.cust_list.append(Customer(uid, 'pin', cb, sb))
        fileObj.close()

    def save_customers(self):
        fileObj = open(self.filename, 'w')
        output_string = ''
        for cust in self.cust_list:
            funcs = [cust.get_id, cust.get_pin, cust.get_cbal, cust.get_sbal]
            for func in funcs:
                if func != cust.get_sbal:
                    fileObj.write(str(func()) + '\t')
                else:
                    fileObj.write(str(func()))
            if cust != self.cust_list[-1]:
                fileObj.write('\n')
        fileObj.close()
class Customer:
    def __init__(self, uid, pin, check_bal, sav_bal):
        self.id = uid
        self.pin = pin
        self.checking_balance = check_bal
        self.savings_balance = sav_bal

    def get_id(self):
        return str(self.id)
    
    def get_pin(self):
        return self.pin
    
    def get_cbal(self):
        return self.checking_balance
    
    def get_sbal(self):
        return self.savings_balance
    
    def withdraw(self, amount, type):
        if type == 'c':
            self.checking_balance -= int(amount)
        else:
            self.savings_balance -=int(amount)

    def deposit(self, amount, type):
        if type == 'c':
            self.checking_balance +=int(amount)
        else:
            self.savings_balance +=int(amount)


def main():
    filename = "atm_accounts.txt"
    atm= ATM(filename)

if __name__ == '__main__':
    main()
        
    
