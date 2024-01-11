"""

"""
print("hello word")
name = "李泽"
print(name)

# input代表输入
userName = input("请输入用户名：")  # 阻塞型函数
print("哈哈啊哈")
print(userName)
print(type(userName))

money = input("请输入缴费金额：")
print(money)
print(type(money))  # 字符串类型
# input为阻塞型函数，执行到此时会中断，左侧亮起红点代表程序未执行完

# 类型转换   str---> int?
print(int(money)+1000)  # 若money后直接+1000会报错，所以必须将money转换成整数型，前面加int包装
print(type(int(money)+1000))
# int ---> str
print(money+str(1000))
print(type(money+str(1000)))  # 字符串与字符串之间只能拼接，不能加减。
