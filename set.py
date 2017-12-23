__author__ = 'Jack Chen'

list1 = [1,4,5,7,3,6,7,9]
list2 = set([2,6,0,66,22,8,4])
list3 = set([1,3,7])
list4 = set([5,6,8])

print('list1:',list1,',','list2:',list2)

print('----處理重複數值----')
list1 = set(list1) #處理重複數值
print(list1)
print('--------------------')

print('----交集----')
print(list1.intersection(list2)) #交集
print(list1 & list2)
print('--------------------')

print('----並集----')
print(list1.union(list2)) #並集
print(list2 | list1)
print('--------------------')


print('----差集----')
print(list1.difference(list2)) #差集 in list1 but no in list2
print(list2.difference(list1)) #差集 in list2 but no in list1
print(list1 - list2) 
print('--------------------')

print('----子集父集----')
print(list1.issubset(list2)) #子集
print(list1.issuperset(list2)) #父集
print(list3.issubset(list1)) #子集
print(list1.issuperset(list3)) #父集
print('--------------------')


print('----對稱差集----')
print(list1.symmetric_difference(list2)) #對稱差集(把各自都沒有的數值給取出來)
print(list1 ^ list2)
print('--------------------')


print('----集合內沒有交集為True----')
print(list3.isdisjoint(list4)) #如果集合內沒有交集為True
print('--------------------')


print('----集合的增刪改查----')
list1.add(999)
list1.update([888,777,555])
print(list1)


print('----集合的刪除----')
list1.discard(888) #刪除集合內一個值，指定的值不在集合內則返回None。
print(list1)
list2.remove(4) #刪除集合內一個值，指定的值不在集合內則會Error。
print(list2)

print(len(list1))
