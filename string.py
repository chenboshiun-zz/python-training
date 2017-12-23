name = 'jack'
string = 'my name is jack'
string2 = 'Hi Jack \tWellcome back'
string3 = "I'm {user} I'm King I'm {year}"

print(name.capitalize()) #子首轉大寫
print(string.count('a')) #計算a的個數
print(name.center(50,'-')) #填滿50字元，不足的用-填滿，並將文字置中
print(name.endswith('ck')) #判斷字尾以哪些字母結尾，符合回傳True，反之False
print(string2.expandtabs(tabsize=30)) #在字串中加入\t，會自動協助轉成相應數量的空格
print(string.find('j')) #回傳字串中的索引值
print(string[string.find('my'):6]) #將字串中的索引值反解成字母，可以指定反解範圍
print(string3.format(user='alex', year=23)) #格式化字串
print(string3.format_map( {'user': 'chris', 'year': 24} )) #利用format_map 把 dict(字典)內容格式化，必較少用
print(string.isalnum()) #字符是否由字母和数字组成=no，不能包含特殊字元
print('ab cd '.isalnum()) #字串是否由字母和数字组成=no
print('ab2000'.isalnum())  #字符是否由字母和数字组成=yes
print('sasai'.isalpha()) #字符串是否只由字母组成=yes 
print('sasai12121'.isalpha()) #字符串是否只由字母组成=no
print('123'.isdecimal()) #字串是否只包含十进制=yes
print('1A'.isdecimal()) #字串是否只包含十进制=no
print('2121'.isdigit()) #字串是否只整數组成=yes
print('2A'.isdigit()) #字串是否只整數组成=no
print('user'.isidentifier()) #字串是否是合法的識別字
print('in'.isidentifier()) #字串是否是合法的識別字，含有空格就回傳False
print('33.33'.isnumeric()) #字串是否是數字，中文英文浮點數皆回傳False
print('sdda'.islower()) #字串是否由小寫字母组成，若是就回傳True，反之回傳False
print('AASA'.isupper()) #字串是否由大寫字母組成，若是就回傳True，反之回傳False
print(' '.isspace()) #字串是否為空格，若是就回傳True，反之回傳False，含有空格的字串也回傳False
print(','.join(['1','2','3','4'])) #把串列中的元素以指定字符連接生成一個新字串
print(name.ljust(50,'*')) #把一个字串向左對齊,并使用字符填充至指定长度的新字串
print(name.rjust(50,'-')) #把一个字串向右對齊,并使用字符填充至指定长度的新字串
print(name.lower()) #把字串轉成小寫
print(name.upper()) #把字串轉成大寫
print('\nAlex'.lstrip()) #去除字串左邊的空格或指定字符
print('Alex\n'.rstrip()) #去除字串右邊的空格或指定字符
print('Alex\n'.strip()) #去除字串頭尾的空格或指定字符
#----maketrans and translate----
p = str.maketrans('aeiou','12345')
print('alex liu'.translate(p)) #用於建立字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标，两个字符串的长度必须相同，为一一对应的关系
print('wonder wong'.replace('w','W')) #可把字串內舊字串替換成新字串，如果指定第三個max參數，則替換字數不超過max參數
print('wonder wong'.rfind('w')) #根據字符，由左至右找出字符的索引值
print('wonder wong'.split()) #根據字串中的空格或指定字元，將字串切片並轉換成串列，也可以指定轉換個數
print('Hi \nthis is \nwonder wong'.splitlines()) #按照換行字符，將字串切片並轉換成串列，也可以指定轉換個數
print('lower to upper'.swapcase(),'UPPER TO lower'.swapcase()) #把字串內的小寫轉大寫或大寫轉小寫
print('wonder wong'.title()) #字串內的字首都是以大寫開始，其餘字母均為小寫
print('wonder liu'.zfill(50)) #印出指定長度的字串，前面填0

