def test(x,y):
    print(x)
    print(y)
#test(y=2,x=1) 關鍵字參數，與位置參數順序無關
#test(1,2) 位置參數與形式參數一一對應
test(3,y=2)
print('-------')
def test(x,y,z):
    print(x)
    print(y)
    print(z)
test(3,z=2,y=6)
