#-*- coding:utf-8 –*-
# 注释中文必须先声明文件的编码信息

'''

#echo -e "\033[41;36m something here \033[0m"
其中41的位置代表底色， 36的位置是代表字的颜色
注： 
　　1、字背景颜色和文字颜色之间是英文的"" 
　　2、文字颜色后面有个m 
　　3、字符串前后可以没有空格，如果有的话，输出也是同样有空格 
　　下面是相应的字和背景颜色，可以自己来尝试找出不同颜色搭配 

　　echo -e “\033[30m 黑色字 \033[0m” 
　　echo -e “\033[31m 红色字 \033[0m” 
　　echo -e “\033[32m 绿色字 \033[0m” 
　　echo -e “\033[33m 黄色字 \033[0m” 
　　echo -e “\033[34m 蓝色字 \033[0m” 
　　echo -e “\033[35m 紫色字 \033[0m” 
　　echo -e “\033[36m 天蓝字 \033[0m” 
　　echo -e “\033[37m 白色字 \033[0m”

　　echo -e “\033[40;37m 黑底白字 \033[0m” 
　　echo -e “\033[41;37m 红底白字 \033[0m” 
　　echo -e “\033[42;37m 绿底白字 \033[0m” 
　　echo -e “\033[43;37m 黄底白字 \033[0m” 
　　echo -e “\033[44;37m 蓝底白字 \033[0m” 
　　echo -e “\033[45;37m 紫底白字 \033[0m” 
　　echo -e “\033[46;37m 天蓝底白字 \033[0m” 
　　echo -e “\033[47;30m 白底黑字 \033[0m”

　　\33[0m 关闭所有属性 
　　\33[1m 设置高亮度 
　　\33[4m 下划线 
　　\33[5m 闪烁 
　　\33[7m 反显 
　　\33[8m 消隐 
　　\33[30m — \33[37m 设置前景色 
　　\33[40m — \33[47m 设置背景色 
　　\33[nA 光标上移n行 
　　\33[nB 光标下移n行 
　　\33[nC 光标右移n行 
　　\33[nD 光标左移n行 
　　\33[y;xH设置光标位置 
　　\33[2J 清屏 
　　\33[K 清除从光标到行尾的内容 
　　\33[s 保存光标位置 
　　\33[u 恢复光标位置 
　　\33[?25l 隐藏光标 
　　\33[?25h 显示光标

'''

#便于后期会增加对日志输入的颜色区分
#定义颜色枚举值

class Colors():
    black = 0  #“\033[30m 黑色字 \033[0m”
    red = 1    #“\033[31m 红色字 \033[0m”
    green = 2  #“\033[32m 绿色字 \033[0m”
    yellow = 3 #“\033[33m 黄色字 \033[0m”
    blue = 4   #“\033[34m 蓝色字 \033[0m”
    purple = 5 #“\033[35m 紫色字 \033[0m”
    sky_blue=6 #“\033[36m 天蓝字 \033[0m”
    white = 7  #“\033[37m 白色字 \033[0m”



def printLog(color,logInfo):
    print getFormatColorLog(color,logInfo)


def getFormatColorLog(color,logStr):
    if color == Colors.black:
        return "\033[30m %s \033[0m" % logStr
    elif color == Colors.red:
        return "\033[31m %s \033[0m" % logStr
    elif color == Colors.green:
        return "\033[32m %s \033[0m" % logStr
    elif color == Colors.yellow:
        return "\033[33m %s \033[0m" % logStr
    elif color == Colors.blue:
        return "\033[34m %s \033[0m" % logStr
    elif color == Colors.purple:
        return "\033[35m %s \033[0m" % logStr
    elif color == Colors.sky_blue:
        return "\033[36m %s \033[0m" % logStr
    elif color == Colors.white:
        return "\033[37m %s \033[0m" % logStr
    else:
        return "\033[37m %s \033[0m" % logStr


# printLog(0,'出来')
# printLog(1,'出来')
# printLog(2,'出来')
# printLog(3,'出来')