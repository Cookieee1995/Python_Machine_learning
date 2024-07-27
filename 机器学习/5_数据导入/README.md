# pima-indians-diabetes

#### 介绍
一、 数据说明： Pima Indians Diabetes Data Set（皮马印第安人糖尿病数据集） 根据现有的医疗信息预测5年内皮马印第安人糖尿病发作的概率。 
数据链接：https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes 



1. 首先我对数据进行了数据探索和数据工程，

分别在【糖尿病预测-数据探索-EDA-train.ipynb】【糖尿病预测-数据工程-FE-train.ipynb】这两个文件中。

然后生成了一个 数据工程后的数据文件【FE_pima-indians-diabetes.csv】。

2. 【糖尿病预测——Logistic回归.ipynb】这个文件中做了Logistics回归，里面用了log损失和准确率两种方法，分别用5折交叉验证对 参数C和penalty进行了超参数调优。并且分别将最佳参数的数据保存到【accuracy_l2.pkl】和【logloss_l1.pkl】以便后续测试使用

