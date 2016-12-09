from checkings import Checkings
from savings import Savings


class Accounts:

    Account_list = []


    def __init__(self, first, last, first_deposit):
        self.first = first
        self.last = last
        self.first_deposit = first_deposit
        self.checkings = Checkings(first_deposit)
        self.savings = Savings(0)
        self.balance = first_deposit
        self.trans_history = ['initial deposit of= ' + str(first_deposit)]
        Accounts.Account_list.append(self)
        Accounts.__str__(self)


    def print_total_balance(self):
        print('checkings bal = ',self.checkings.balance)
        print('savings bal = ',self.savings.balance)
        total_bal = self.checkings.balance + self.savings.balance
        return total_bal

    def print_total_trans_hist(self):
        self.trans_history.append(self.checkings.trans_history)
        self.trans_history.append(self.savings.trans_history)

        print(self.trans_history)


    def print_trans_hist(self, account):
        if account == 'checkings':
            print(self.checkings.trans_history)
        elif account == 'savings':
            print(self.savings.trans_history)


    def transfer_out(self, to_acct, amt):
        to_acct.checkings.balance += amt
        to_acct.balance += amt
        to_acct.checkings.trans_history.append('Received Transfer = ' + str(amt))

        self.checkings.balance -= amt
        self.balance -= amt
        self.checkings.trans_history.append('Transferred Out = ' + str(amt))


    def transfer_between(self, to_acct, amt):
        if to_acct == 'savings':
            self.checkings.balance -= amt
            self.balance -= amt
            self.checkings.trans_history.append('Transferred to Savings = ' + str(amt))


            self.savings.balance += amt
            self.balance += amt
            self.savings.trans_history.append('Transferred from Checkings = ' + str(amt))


        elif to_acct == 'checkings':
            self.savings.balance -= amt
            self.balance -= amt
            self.savings.trans_history.append('Transferred to Checkings = ' + str(amt))


            self.checkings.balance += amt
            self.balance += amt
            self.checkings.trans_history.append('Transferred from Savings = ' + str(amt))


    def deposit(self, to_acct, amt):
        if to_acct == 'checkings':
            self.checkings.balance += amt
            self.balance += amt
            self.checkings.trans_history.append('Deposited = ' + str(amt))

        elif to_acct == 'savings':
            self.savings.balance += amt
            self.balance += amt
            self.savings.trans_history.append('Deposited = ' + str(amt))

    def withdraw(self, to_acct, amt):
        if to_acct == 'checkings':
            self.checkings.balance -= amt
            self.balance -= amt
            self.checkings.trans_history.append('Withdrew = ' + str(amt))

        elif to_acct == 'savings':
            self.savings.balance -= amt
            self.balance -= amt
            self.savings.trans_history.append('Withdrew = ' + str(amt))

    def apply_interest(self):
        accrued = (self.savings.balance * Savings.interest_rate)
        self.savings.balance += accrued
        self.balance += accrued
        self.savings.trans_history.append('Interest amount earned = ' + str(accrued))


    def __repr__(self):
        return 'Account %s %s %s' % (self.first, self.last, self.balance)
