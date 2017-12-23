'''school = 'oldboy'
names = ['jack', 'wayne', 'alex']
def changeName():
    names[0] = 'JMD'
    print(names)

changeName()
print(names)
# 除了字串，整數，元祖不能在函數做更改，串列，字典，集合可以更改
'''

'''school = 'oldboy' #全局變量
def changeName():
    global name
    name = 'Jack'

changeName()
print(name)
'''
'''
def changeName(name):
    global school
    school = 'Maga Linux'
    print('before name:', name,school)
    name = 'Wayne' #局部變量，只在函數生效，這個函數就是這個變量的作用域
    age = 22
    print('after name:', name)
    print('age:', age)

name = 'JMD'
changeName(name)
print(name)
print(school)
'''
'''def test(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST!!")

def logger(source):
    print('form %s' % source)

test('jack',age=34,sex='M',car='YAMAHA')
'''
