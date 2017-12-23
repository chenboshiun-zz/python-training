#-*- coding:utf-8 -*-
import sys
print(sys.getdefaultencoding()) #顯示目前編碼

#正解(utf-8 to unicode to gbk)

s = u"您好" #已宣告字符為unicode

#s_to_unicode = s.decode('utf-8')
#print(s_to_unicode)



s_to_gbk = s.encode('gbk')
print(s_to_gbk)

print('----break----')

#反解(gbk to unicode to utf-8)

gbk_to_utf8 = s_to_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)


#s_to_unicode = s.decode('utf-8')
#print(s_to_unicode) 
#s_to_gbk = s_to_unicode.encode('gbk')
#print(s_to_gbk)
