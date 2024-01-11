"""
类型转换练习：
键盘输入两个整数的和，输出差
input("输入第一个数：")
input("输入第二个数：")
"""
one = input("输入第一个数：")
two = input("输入第二个数：")  # 其中括号里面的汉字为提示语句
print(one+two)  # 回车并输入数字后变成2980，而不是109，这是由于Input键盘输入的都是字符串类型，
# 若想进行数与数之间的运算只能转换
# 转换
print(int(one)+int(two))  # 整型
print(float(one)+float(two))  # 浮点型
# 上面两个数若输入小数则会报错

"""
总结：
以变量a为例
str ---> int  若a为字符串类型则int(a).但若a为带小数点的字符串类型如“9.9”转成int会报错 
str ---> float  float(a)
int ---> str  str(a)
float ---> str  str(a)
int ---> float  float(a)
float ---> int   int(a)  只不过float类型中小数点后面的数字被抹掉了
"""
flag = True
# bool ---> int   True转整型对应1，False对应0
print(int(flag))
print(float(flag))
print(str(flag))  # 还是输出True 只不过是加引号的“True”

# 当变量的值是0或“”（空字符串），转换结果为Flase,其他只要变量有值则为True


