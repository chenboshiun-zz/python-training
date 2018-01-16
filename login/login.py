info = {
        'jack':'1212',
        'wayne':'3434'
}
lock = {}
cache = {}
count = 0

while count < 3:
    user = input('account:')
    if user not in info.keys():
        print('Can\'t find your account!!!')
        continue
    elif user in cache.keys() and 'C' in list(cache.values()):
        print('Already login, welcome to account sysyem')
        break
    elif user in lock.keys() and 'L' in list(lock.values()):
        print('%s is locked!!, please contract Admin' % user)
        continue
    pwd = input('password:')
    if user in info.keys() and pwd in list(info.values()):
        print('Login successfully!!!，welcome to account sysyem')
        with open('account.txt','w+') as f:
            cache.setdefault(user,'C')
            f.write(user)
        reLogin = input('Do you want to relogin[Y/N]:')
        if reLogin != 'N' and reLogin != 'n':
            count = 0
        else:
            print('Welcome to account sysyem')
            break
    else:
        print('Password error, please re-type your password')
    count += 1
    if user in info.keys() and count == 3:
        print('Auth Error 3, lock %s!!!, Please contact admin' % user)
        lock.setdefault(user,'L')
        reLogin = input('Do you want to relogin[Y/N]:')
        if reLogin != 'N' and reLogin != 'n':
            count = 0
        else:
            print('Welcome back again')
            break
