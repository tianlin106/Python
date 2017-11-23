# -*- coding:utf-8 –*-

import sys
import _List
import string
import PKLog


money = 0

PKLog.printLog(PKLog.Colors.black,money)
while 1:
    moneyInput = raw_input(PKLog.getFormatColorLog(2, "请输入money"))
    try:
        money = int(moneyInput)
    except:
        PKLog.printLog(PKLog.Colors.red,'输入类型错误！，请重新输入')
    else:
        if money < 0:
            continue
        else:
            break
    finally:
        PKLog.printLog(PKLog.Colors.sky_blue, '\n')



listDict = {'banala':25,'apple':16,'orange':8,'lemon':13.5,'watermelon':9.5}
# print listDict.values()[0]

cart = []

# if remainMoney < 0:
#     PKLog.printLog(PKLog.Colors.yellow, '余额不足，请及时充值')
#     break
# else:

while 1:
    for i in range(0, listDict.values().__len__()):
        remainMoney = money - listDict.values()[i]
        if remainMoney > 0:
            PKLog.printLog(PKLog.Colors.blue, '您可以购买%s' % listDict.keys()[i])
            continue
        else:
            if i == 0:
                PKLog.printLog(PKLog.Colors.yellow, '余额不足，请及时充值')
    break






