# -*- coding:utf-8 –*-

import _File
import fileinput
import _List


# "we"
filePath = open("student")

fileLines = filePath.readlines()

print fileLines

while 1:
    searchKey = raw_input("please input search keywords:")
    if searchKey.strip().__len__() < 1:
        continue;
    for item in fileLines:
        print  item

    else:
        print "not find"
        break



# "read"
# li = []
# print li.__len__()
# li.append("qiqi")
# li.append("eeee")
# print li
# li.insert(0,"dfsd")
# print li[1]
# li.insert(li.__len__(),'dfsdf')
# print li
# li[2] = 'pingkang'
# print  li
# li.pop(li.__len__() - 1)
# print li
# print li.index('pingkang')
