info = {
        # key    account | pwd | lock | cache | create |
        'user1' : ['jack','1212','E','','C'],
        'user2' : ['wayne','1212','E','','C'],
}
import getpass
inputcount = 0

for i in info:
    data = i

while inputcount < 3:
    user = input('account:')
    if user != info[data][0]:
        print('Can\'t find your account!!!')
        continue 
    elif user == info[data][0] and info[data][3] == 'Y' and info[data][4] == 'C':
        print('login successfully!!!，Welcome to account sysyem')
        with open('account.txt','w+') as f:
            f.write(info[data][0])
            f.write(',')
            f.write(info[data][2])
            f.write('\n')
        break
    elif user == info[data][0] and info[data][2] == 'D':
        print('%s is locked!!, please contract Admin' % user)
        break
    pwd = getpass.getpass('password:')
    if user == info[data][0] and pwd == info[data][1] and info[data][4] == 'C':
        print('login successfully!!!，Welcome to account sysyem')
        info[data][3] = 'Y'
        choice = input('want to logout[Y/N]:')
        if choice != 'n' and choice != 'N':
            inputcount = 0
        else:
            print('Welcome to account sysyem')
            break
    else:
        print('password error, please re-type your password')
    inputcount += 1
    if user == info[data][0] and inputcount == 3: 
        print('Error 3, lock user!!!')
        info[data][2] = 'D'
        reLogin = input('Want to reloagin[Y/N]:')
        if reLogin != 'N' and reLogin != 'n':
            inputcount = 0
        else:
            print('Welcome back again')
            break
