#!/usr/bin/env python3.6
'''
with open('song2', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
'''
import sys

findStr = sys.argv[1]
replaceStr = sys.argv[2]
'''
f = open('song2', 'r', encoding='utf-8')
fNew = open('song2.bak', 'w', encoding='utf-8')
'''
with open('song2','r',encoding='utf-8') as f, \
     open('song2.bak' ,'w',encoding='utf-8') as fNew:
         for line in f:
             if findStr in line:
                 line = line.replace(findStr,replaceStr)
             fNew.write(line)
#f.close()
#fNew.close()

