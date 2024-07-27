from numpy import loadtxt
# 使用标准的 NumPy 导入CSV数据
filename = 'pima_data.csv'
with open(filename,'rt') as raw_data:
    data = loadtxt(raw_data,delimiter=',')
    print(data.shape)