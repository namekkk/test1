#作业
import random
from turtledemo.nim import computerzug

player=int(input('请输入数字，1，2，3'))
computer=random.randint(1,3)
print(f'{computer}')
if(player==1 and computer==2)or(player==2 and computer==3)or(player==3 and computer==1):
    print('你赢了')
elif player ==computer:
    print('平局')
else:
    print('你输了')


# pwd=input('请输入密码')
# if pwd=='123456':
#     money=int(input('请输入取款金额'))
#     if money<=1000:
#         print('取款成功')
#     else:
#         print('金额不足')
# else:
#     print('取款失败')

# score=int(input('请输入分数'))
# if score>90:
#     print('优')
# elif score>=80 and score<=90:
#     print('良')
# name=input('请输入姓名')
# if name=='admin'or name=='test':
#     print(f'欢迎{name}登录')
# else:
#     print('查无此人')

# name=input('请输入用户名')
# pwd=input('请输入密码')
# if name=='admin'and pwd=='123456':
#     print('登录成功')
# else:
#     print('登录信息错误')
# name=input('请输入姓名')
# if name=='admin':
#     print('欢迎admin')
# else:
#     print('用户名错误')
# age=input('请输入年龄')
# if int(age)>18:
#     print('大于18岁可以进入网吧')
# else:
#     print("小于18岁不可以进入网吧")
# name=input('请输入姓名')
# if name=='admin':
#     print('欢迎admin')
# age=input('请输入年龄')
# if int(age)>18:
#     print('大于18可以进入网吧')
# print("直接")

# num1=input('请输入第1个数字')
# num2=input('请输入第2个数字')
# num=int(num1)+int(num2)
# print(num)
