# Python 速成
# 字符串
data = 'Hello,world!'
print(data[0])
print(data[1:5])
print(len(data))
print(data)

# 数值
value = 6.18
print(value)

# 布尔类型
true = True
false = False
print(true)
print(false)

# 多变量赋值
a,b,c = 1,'hello',True
print(a,b,c)
print(a)
print(b)
print(c)

# 空值
a = None
b = a
print(a)
print(b)

# 条件控制语句
value = 1
if value == 1:
    print('This is true')
elif value > 10:
    print('it is bigger than 10?Yes it is true.')
else:
    print('This is false')

# 循环语句
for i in range(5):
    print(i)

# 条件循环语句
i = 0
while i < 5:
    print(i)
    i += 1

# 元组
a = (1,2,3)
print(a)
print(a[1])

# 列表
a = [1,2,3]
print(a)
# 增加列表项
a.append(4)
print(a)
print(a[3])
# 更新列表项
a[2] = 5
print(a)
for i in a:
    print(i)

# 字典
mydict = {'a':6.18,'b':'str','c':True}
print('A value:%.2f' % mydict['a'])
# 增加字典元素
mydict['a'] = 523
print('A value: %d' % mydict['a'])
print('keys: %s' % mydict.keys())
print('values: %s' % mydict.values())
for key in mydict:
    print(mydict[key])

mydict = {'a':6.18,'b':'str','c':True}
# 删除特定元素
mydict.pop('a')
print(mydict)
# 删除字典中的全部元素
mydict.clear()
print(mydict)

# 定义函数
def mysum(x,y):
    "这是自定义函数"
    return x+y
# 测试函数
result = mysum(x=1,y=2)
print(result)

with open('somefileName') as somefile:
    for line in somefile:
        print(line)
        # ...more code

somefile = open('somefileName')
try:
    for line in somefile:
        print(line)
        # ...more code
finally:
    somefile.close()