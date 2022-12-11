from datetime import datetime
from enum import Enum


class Currency(float, Enum):
    USD_KZT_rate = 473
    EUR_rate = 495
    RUB_rate = 7.31
    EUR_USD_rate = 1.05
    EUR_RUB_rate = 65.84


class Bank:

    def __init__(self):
        self.total_amount = 0
        self.name = ''
        self.surname = ''

    def welcome(self):
        self.name, self.surname = input('Welcome to your Bank Account. '
                                        '\nPlease Enter your name and surname : ').split(' ')
        self.current_time = datetime.now()
        self.stamp = datetime.timestamp(self.current_time)
        self.objectdate = datetime.fromtimestamp(self.stamp)

    def ToString(self):
        print(f'Dear {self.name}, your current balance is : {self.total_amount}')
        print(f'Account data creation is: {self.objectdate}')

    def addToBankAccount(self):
        self.total_amount += float(input('Hello {}, please enter amount: '.format(self.name, self.surname)))
        self.ToString()

    def subtractFromBankAccount(self):
        amount_to_withdraw = float(input('Enter amount to withdraw: '))

        if amount_to_withdraw > self.total_amount:
            print('Insufficient Balance !!')
        else:
            self.total_amount -= amount_to_withdraw

        self.ToString()

    def moneyConversion(self):
        cur_currency = int(input('what currency do you want to change?'
                                 '\n 1 - KZT > USD'
                                 '\n 2 - KZT > EUR'
                                 '\n 3 - KZT > RUB'
                                 '\n 4 - USD > KZT'
                                 '\n 5 - USD > EUR'
                                 '\n 6 - USD > RUB'
                                 '\n 7 - EUR > KZT'
                                 '\n 8 - EUR > USD'
                                 '\n 9 - EUR > RUB'
                                 '\n 0 - BACK\n'))

        if int(cur_currency) == 1:
            KZT_amount = float(input('how many KZT do you want to change to USD?\n'))
            print(f'You will receive {round(KZT_amount / Currency.USD_KZT_rate)} dollars')
        elif int(cur_currency) == 2:
            KZT_amount = float(input('how many KZT do you want to change to EUR?\n'))
            print(f'You will receive {round(KZT_amount / Currency.EUR_rate)} euros ')
        elif int(cur_currency) == 3:
            KZT_amount = float(input('how many KZT do you want to change to RUB?\n'))
            print(f'You will receive {round(KZT_amount / Currency.RUB_rate)} rubles ')

        elif int(cur_currency) == 4:
            USD_amount = float(input('how many USD do you want to change to KZT?\n'))
            print(f'You will receive {round(USD_amount * Currency.USD_KZT_rate)} dollars')
        elif int(cur_currency) == 5:
            USD_amount = float(input('how many USD do you want to change to EUR?\n'))
            print(f'You will receive {round(USD_amount / Currency.EUR_USD_rate)} euros ')
        elif int(cur_currency) == 6:
            USD_amount = float(input('how many USD do you want to change to RUB?\n'))
            print(f'You will receive {round(USD_amount * Currency.EUR_RUB_rate)} rubles ')

        elif int(cur_currency) == 7:
            EUR_amount = float(input('how many EUR do you want to change to KZT?\n'))
            print(f'You will receive {round(EUR_amount * Currency.EUR_rate)} tenge')
        elif int(cur_currency) == 8:
            EUR_amount = float(input('how many EUR do you want to change to USD?\n'))
            print(f'You will receive {round(EUR_amount / Currency.EUR_USD_rate)} dollars ')
        elif int(cur_currency) == 9:
            EUR_amount = float(input('How many EUR do you want to change to RUB?\n'))
            print(f'You will receive {round(EUR_amount * Currency.EUR_RUB_rate)} rubles ')
        else:
            print(input_value)


if __name__ == "__main__":
    bank = Bank()
    bank.welcome()

while True:
    input_value = int(input('Choose your preferred operation:'
                            '\n1 - Display account information and balance'
                            '\n2 - Add to balance '
                            '\n3 - Subtract from balance '
                            '\n4 - Currency exchange service'
                            '\n5 - Account information\n'))
    if input_value == 1:
        bank.ToString()
    elif input_value == 2:
        bank.addToBankAccount()
    elif input_value == 3:
        bank.subtractFromBankAccount()
    elif input_value == 4:
        bank.moneyConversion()
    elif input_value == 5:
        bank.ToString()
    else:
        print('Please enter a valid input.')
