
from account import Accounts

def main():
    Acct1 = Accounts('Homie', 'G', 15000)
    Acct2 = Accounts('P.', 'Diddy', 8000)
    Acct3 = Accounts('Django', 'Reinhardt', 4000 )
    Acct4 = Accounts('Wes', 'Montgomery', 50000)
    Acct5 = Accounts('Emily', 'Remler', 90000)

    menu_options = ('1. Deposit \n2. Withdraw \n3. Transfer Between \n\
4. Transfer Out \n5. Print Balance \n6. Print Account History \n\
7. Apply Accrual Interest \n8. Change Account \n9. Quit')

    print("Choose one of the following accounts by entering the number on the \
left \n")
    counter = 0
    for i in Accounts.Account_list:
        counter += 1
        print(counter, i)

    account_index = int(input("\nWhat account do you want to play with? > \n"))
    account_choice = Accounts.Account_list[account_index - 1]

    user_option = 0

    while user_option != 9:
        print(account_choice)
        print('\n')

        print('Enter in the number to choose one of the following options.\n')
        print(menu_options)
        user_option = int(input('\n > '))
        if user_option < 1 or user_option > 9:
            print(account_choice)
            print('\n')
            print('Enter in the number to choose one of the following options\n')
            print(menu_options)
            user_option = int(input('\n > '))

        #Deposit menu option
        elif user_option == 1:
            print('Deposit into (c)heckings or (s)avings?')
            c_or_s = input(' > '.lower())
            if c_or_s == 'c':
                print('How much?')
                amount = int(input(' > '))
                account_choice.deposit('checkings', amount)
            elif c_or_s == 's':
                print('How much?')
                amount = int(input(' > '))
                account_choice.deposit('savings', amount)

        #Withdraw menu options:
        elif user_option == 2:
            print('Withdraw from (c)heckings or (s)avings?')
            c_or_s = input(' > '.lower())
            if c_or_s == 'c':
                print('How much?')
                amount = int(input(' > '))
                account_choice.withdraw('checkings', amount)
            elif c_or_s == 's':
                print('How much?')
                amount = int(input(' > '))
                account_choice.withdraw('savings', amount)

        #Transfer Between Checkings and Savings option
        elif user_option == 3:
            print('Okay, you want to transfer between checkings and savings\n')
            print('Do you want to transfer to (c)heckings or (s)avings')
            c_or_s = input(' > '.lower())
            if c_or_s == 'c':
                print('How much?')
                amount = int(input(' > '))
                account_choice.transfer_between('checkings', amount)
                print(account_choice.checkings.balance)
                print(account_choice.savings.balance)
            elif c_or_s == 's':
                print('How much?')
                amount = int(input(' > '))
                account_choice.transfer_between('savings', amount)
                print(account_choice.checkings.balance)
                print(account_choice.savings.balance)

        #Transfer out option
        elif user_option == 4:
            print('Whom do you want to transfer money to?')
            counter = 0
            for i in Accounts.Account_list:
                counter += 1
                if i == account_choice:
                    continue
                print(counter, i)
            other_index = int(input('\nSame deal, which account? > '))
            other_account = Accounts.Account_list[other_index - 1]
            print('\nYou chose')
            print(other_account)
            amount = int(input('How much would you like to transfer? > '))
            account_choice.transfer_out(other_account, amount)

        #Print Balance option
        elif user_option == 5:
            print('(C)heckings balance, (S)avings balance, or (T)otal Balance')
            s_c_t = input(' > '.lower())
            if s_c_t == 's':
                print(account_choice.savings.balance)
            elif s_c_t == 'c':
                print(account_choice.checkings.balance)
            elif s_c_t == 't':
                account_choice.print_total_balance()

        #Print account history option
        elif user_option == 6:
            print('(c)heckings history, (s)avings history, or (t)otal history?')
            s_c_t = input(' > '.lower())
            if s_c_t == 's':
                account_choice.print_trans_hist('savings')
            elif s_c_t == 'c':
                account_choice.print_trans_hist('checkings')
            elif s_c_t == 't':
                account_choice.print_total_trans_hist()

        #Apply accrual interest option
        elif user_option == 7:
            account_choice.apply_interest()

        #Change account option
        elif user_option == 8:
            print('Which account do you want to switch to?')
            counter = 0
            for i in Accounts.Account_list:
                counter += 1
                if i == account_choice:
                    continue
                print(counter, i)
            account_index = int(input('Same deal, which account? > '))
            account_choice = Accounts.Account_list[account_index - 1]
            print('\nYou chose')
            print(account_choice)

        print('Hope you had fun, come back anytime!')





main()
