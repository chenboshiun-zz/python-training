__author__ = "Jack Chen"

import sys
print(sys.getdefaultencoding())

s = "你哈" #在python3中已經是unicode(utd-8)格式
s_to_gbk = s.encode('gbk')
print('GBK:',s_to_gbk)
print('UTF-8:',s.encode())
gbk_to_utf8 = s_to_gbk.decode('gbk').encode('utf-8')
print(gbk_to_utf8)
#print(s.encode('gbk'))
#print(s_to_gbk)
#print(s.encode())

