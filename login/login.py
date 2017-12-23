info = {
        'user1' : ['jack','1212'],
}
count = 0


while count < 3:
    user = input('account:')
    pwd = input('password:')
    for i in info:
        data = i
    if user == info[data][0] and pwd == info[data][1]:
        print('YES')
        with open('account.txt','w+') as f:
            f.write(user)
        break
    else:
        print('NO')
    count += 1
    if count == 3:
        print('Error 3, lock user!!!')
        with open('locked.txt','w+') as l:
            l.write(user)
            l.write('\n')
            reLogin = input('Want to reloagin[Y/N]:')
            if reLogin != 'N' and reLogin != 'n':
                count = 0
else:
    print('Welcome back')
