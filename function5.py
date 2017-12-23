#kwargs: 把N個關鍵字參數轉換成字典的方式

def test5(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test5('jack',age=34,sex='M',car='YAMAHA')
'''
def test3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])
test3(name='alex',age=8,sex='M')
test3(**{'name':'jack','age':8,'sex':'M'})'''
'''
def test4(name,age=18,**kwargs): #**kwargs一定要放在最後面
    print(name)
    print(age)
    print(kwargs)

test4('alex',sex='F',hobby='tesla',age=3)
'''

'''def test2(x,*args):
    print(x)
    print(args)

test2(1,2,43,54,89,55,77)'''


'''def test(*args): #在參數不固定情況下可以用def test(*args)，來給予值
    print(args)


test(1,2,3,4,5,5)
test(*[1,2,3,3,44,6]) #args=tuple(1,2,3,3,44,6)
'''

'''def test(x,y):
    print(x)
    print(y)

test(1)
'''

'''
def test(x,y=2): #定義形式參數時就預先給形參賦值
    print(x)
    print(y)
test(1) #也可以用關鍵字參數或位置參數賦值
'''
'''
預設參數特點:
1.調用參數時，默認參數非必須賦予
2.用途:預設安裝，預設值
'''
