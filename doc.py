# f.read() 讀取文件內所有內容，模式b為二進制讀取，t為文本模式
# f.readline() 讀取指定line數的文件內容，預設讀一行，指定數值後只讀取到指定字元數
# f.readlines() 讀取文件內的所有行並將內容用串列的形式輸出，常用for in 迴圈處理
# f.write() 文件中写入指定字符串
# f.writelines() 把串列寫入文件中
# for line in f: #讀取效率最高的方式，也是最常用的方式
# str.strip() #用于移除字符串头尾指定的字符（默认为空格）
# f.tell() 返回文件的当前位置，即文件指针当前位置
# f.seek() 用于移动文件读取指针到指定位置，預設值0
# f.encoding() 檢查文件的編碼方式
# f.buffer()
# f.errors()
# f.fileno() 這個是作業系統專門的接口，專門去調度系统的 I/O 操作，這個接口是提供給所有程式語言使用，並不是Python才會有的 
# f.name() 顯示文件名
# f.isatty() 判斷是否為終端設備，若是返回True
# f.seekable() 判斷文件是否可移動讀取位置，若是返回True，反之False
# f.readable() 判斷文件是否可讀，若是返回True
# f.writeable() 判斷文件是否可寫，若是返回True
# f.flush() 讀寫即時刷新，用於進度條，重要！！ 
# f.closed() 判斷文件是否關閉
# f.newlines()
# f.truncate() 在指定位置截斷文件內的字串，不受seek影響


'''
f = open('foo.txt', 'rb')
print(f.readline().)
print(f.readline())
print(f.readline())
f.close()
'''
'''
f = open('foo.txt', 'a+')
print('current initial location:', f.tell())
f.write("----------我是第一行----------\n")
f.write("----------我是第二行----------\n")
f.write("----------我是第三行----------\n")
f.write("----------我是第四行----------\n")
f.write("----------我是第五行----------\n")
print('current location:', f.tell())
f.seek(10)
print('back location:', f.tell())
print(f.readline())
print(f.read())
f.write('I am Jack\n')
print('last location:', f.tell())
f.close()
'''


'''
f = open('foo.txt', 'a', encoding='utf-8')
f.seek(10)
f.truncate(7)
'''

'''
import sys, time

for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)
'''

'''
f = open('song3','wb')
f.write('hello binary\n'.encode())
f.close()
'''

'''
f = open('song','r')
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(10)
print(f.readline())
print(f.encoding)
print(f.flush())
'''

'''
f = open('song','r')
count = 0
for line in f:
    if count == 9:
        print('-------我是分隔線-------')
        count += 1
        continue
    print(line)
    count += 1
'''

'''
f = open('song','r')

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('--我是分隔線--')
        continue
    print(index,line.strip())

for i in range(5):
    print(f.readline())
'''


