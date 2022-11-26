def ToBankAccountOperation(add_money, sub_money):
    cur1 = None
    cur1 = float(input("How much money do you want to add?"))
    print(f'Your added:{cur1}')
    cur2 = float(input("How much money do you want to subtract?"))
    print(f'Your are subtracting:{cur2}')
    return cur1 - cur2

print(f'Total account sum is: {ToBankAccountOperation(None,None)}'
      '\nThanks you for using our Bank operation')

def moneyConversion(money, USD, KZT):
    USD_to_tenge = 470
    cur_choose = int(input('What currency do you have?\n 1 - USD, 2 - KZT \n'))
    if int(cur_choose) == 1:
        money = float(input('how many USD do you want to change to KZT?\n'))
        res = money * USD_to_tenge
        return round(res)
    elif int(cur_choose) == 2:
        money = float(input('how many KZT do you want to change to USD?\n'))
        res = money / USD_to_tenge
        return round(res)

print(f'You will recieve:{moneyConversion(None, None, None)}')



