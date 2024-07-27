# 显示数据的相关性
filename = 'pima_data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename,names=names)
# 设置数据的精确度
pd.options.display.precision = 2
print(data.corr(method='pearson'))