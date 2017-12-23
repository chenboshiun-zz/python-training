productionList = [
        ('iphone', 5800),
        ('MacPro', 9800),
        ('Bike', 800),
        ('Coffee', 30),
        ('Python Cookbook', 120),
]
shoppingList = []

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(productionList):
            print(index,item)
        userChoice = input('是否購買?>>>:')
        if userChoice.isdigit():
            userChoice = int(userChoice)
            if userChoice < len(productionList) and userChoice >= 0:
                pItem = productionList[userChoice]
                if pItem[1] <= salary:
                    shoppingList.append(pItem)
                    salary -= pItem[1]
                    print('Added %s into shopping cart, your currect balance is \033[31:1m%s\033[0m' %(pItem,salary))
                else:
                    print('\033[41:1mYour current balances[%s], sorry\033[0m' % salary)
            else:
                print('production [%s] is not exist')
        elif userChoice == 'q':
            print('exit...')
            print('------')
            for p in shoppingList:
                print(p)
            print('your current balance:',salary)
            exit()
        else:
            print('Invalid option')


