info = {
        'user1' : ['jack','1212','E','0'],
}
count = 0

for i in info:
    data = i

exit_flag = False

while count < 3 and not exit_flag:
    user = input('account:')
    pwd = input('password:')
    if user == info[data][0] and info[data][2] == 'D':
        print('%s is locked!!, please contract Admin' % user)
        break
    elif user == info[data][0] and pwd == info[data][1]:
        print('login successfully!!!')
        with open('account.txt','w+') as f:
            f.write(user)
            f.write('\n')
        choice = input('want to logout[Y/N]')
        if choice != 'N' and choice != 'n':
            exit_flag = True
        else:
            print('Welcome back~')
            break
    else:
        print('auth error, please re-type account and password')
    count += 1
    if count == 3:
        print('Error 3, lock user!!!')
        info[data][2] = 'D'
        reLogin = input('Want to reloagin[Y/N]:')
        if reLogin != 'N' and reLogin != 'n':
            count = 0
else:
    print('Bye Bye~')
