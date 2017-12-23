productionList = [
        ('iphone6', 20000),
        ('iphone7', 30000),
        ('MacPro', 45505),
        ('MacAir', 35505),
        ('Coffee', 120),
        ('Cookie', 35),
]

cart = []
total = 0

salary = input('please type in your salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        print(end='\n')
        print('----The following is my store production, select your need item----',end='\n\n')
        for index, item in enumerate(productionList):
            print(index, item)
        print(end='\n')
        confirmBuy = input('do you want to buy[Y/N]:')
        if confirmBuy == 'Y' or confirmBuy == 'y':
            print(end='\n')
            userChoice = input('please select your item or exit[q]:')
            if userChoice.isdigit():
                userChoice = int(userChoice)
                if userChoice < len(productionList) and userChoice >= 0:
                    pItem = productionList[userChoice]
                    if pItem[1] <= salary:
                        cart.append(pItem)
                        salary -= pItem[1]
                        total += pItem[1]
                        print('Added %s into shopping cart, your currect balance is \033[31:1m%s\033[0m' %(pItem,salary))
                    else:
                        print('\033[41:1mYour current balances[%s], sorry\033[0m' % salary)
                else:
                    print(end='\n')
                    print('production [%s] is not exist' % userChoice)
            elif userChoice == 'q':
                for p in cart:
                    print(p)
                print('purchase total %s,your current balance: %s' %(total, salary))
                print('Welcome Back again')
                exit()
            else:
                print('Invalid option')
                continue
        elif confirmBuy == 'N' or confirmBuy == 'n':
            print(end='\n')
            print('----The following is your shopping cart----')
            for p in cart:
                print(p)
            print('--------------------------------------------')
            print('purchase total %s, your current balance: %s' %(total, salary))
            print(end='\n')
            print('Welcome Back again')
            exit()
        else:
            print('Invalid option')
            continue
else:
    print('please re-type in your salary')
    exit()
