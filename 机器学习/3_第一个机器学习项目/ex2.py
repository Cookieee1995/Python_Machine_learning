# 导入数据
from pandas import read_csv
filename = 'iris.data.csv'
names = ['separ-length','separ-width','petal-length','petal-width','class']
dataset = read_csv(filename,names=names)