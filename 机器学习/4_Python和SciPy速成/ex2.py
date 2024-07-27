# NumPy 速成
import numpy as np
# 创建数组
myarray = np.array([1,2,3])
print(myarray)
print(myarray.shape)
# 创建多维数组
myarray = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(myarray)
print(myarray.shape)

# 访问数据
print('这是第一行：%s' % myarray[0])
print('这是最后一行：%s' % myarray[-1])
print('访问整列（3列）数据：%s' % myarray[:,2])
print('访问指定行（2行）和列（3列）的数据：%s' % myarray[1,2])

myarray1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
myarray2 = np.array([[11,21,31],[21,31,41],[31,41,51]])
print('向量加法运算：')
print(myarray1+myarray2)
print('向量乘法运算：')
print(myarray1*myarray2)
