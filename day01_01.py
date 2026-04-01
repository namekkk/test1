name='小明'
age=18
height=1.71
print('我的名字是 %s,年龄是 %d，身高是%f m'%(name,age,height))
print('我的名字是 %s,年龄是 %d，身高是%.2f m'%(name,age,height))
print('我的名字是 %s,年龄是 %d，身高是%.1f m'%(name,age,height))
stu_num=1
print('我的学号是%d' %stu_num)
print('我的学号是%06d' %stu_num)
num=90
print('某次考试的及格率为 %d%%'%num)
print(f'我的名字是{name},年龄是{age},本次考试的及格率为{num}%')
print('我的名字是 {}, 年龄是 {}, 身高是 {} m, 学号 {}, 本次考试的及格率为 {}%'.format(name,age,height,stu_num,num))
#print('我的名字是{},年龄是{},身高是{height:.3f}m'.format(name,age,height))
print('我的名字是 {}, 年龄是 {}, 身高是 {:.3f} m, 学号 {:06d}, 本次考试的及格率为 {}%'.format(name, age, height, stu_num, num))



