total = 0
myItem = []
storeItem = [['0','iphoneX',30000],['1','iphone7',20000],['2','gogoro',87000]]

print('Please type in your saving:')
salary = int(input('Salary:'))
print("Your saving:", salary,end='\n\n')
while salary >= 0:
    print('----The following is my store production, select your need item----',end='\n\n')
    for i in storeItem:
        print(i)
    print(end='\n')
    buyItem = int(input("Please type in item seq:"))
    compareValue = storeItem[buyItem][2] 
    if salary >= compareValue:
        salary -= compareValue
        total += compareValue
        print('Added',storeItem[buyItem][1],'to your shopping cart')
        myItem.append((storeItem[buyItem][1]))
    else:
        print('Your saving not enought')
    print(end='\n')
    confirmBuy = input('Do you want to buy again[Y/N]:')
    print(end='\n')
    if confirmBuy == 'N' or confirmBuy == 'n':
        print('----The following is your shopping cart----')
        for x in myItem:
            print(x)
        print('--------------------------------------------')
        print('Total:', total, 'Remaining Salary:', salary)
        print(end='\n')
        print('Wellcome back IT shopping again')
        break
else:
    print("Wellcome back IT shopping")



    



