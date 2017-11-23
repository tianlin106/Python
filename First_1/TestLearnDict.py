#-*- coding:utf-8 –*-
# 注释中文必须先声明文件的编码信息

import sys
import fileinput
import string

import PKLog


filePath = open("DictTest")
listInfo = filePath.readlines()
PKLog.printLog(1,listInfo)



while 1:
    searchKey = raw_input(PKLog.getFormatColorLog(PKLog.Colors.purple,'请输入要要找的内容'))


    for i in range(0,listInfo.__len__()):
        print  type(listInfo[i])
        dictInfo = eval(listInfo[i])   #将字符串转成字典
        if type(dictInfo) == dict:
            for key,value in dictInfo.items():
                # print 'sdffsf'
                # PKLog.printLog(PKLog.Colors.blue,PKLog.getFormatColorLog(PKLog.Colors.blue,'key = %s'%key + '   value = %s'% value))
                if key == 'name' and searchKey in value:
                    PKLog.printLog(PKLog.Colors.green,'找到符合条件的项目 %s'%dictInfo + '  name = %s'%value)