# 分离数据集
# array = dataset.values
# X = array[:,0:4]
# Y = array[:,4]
# validation_size = 0.2
# seed = 7
# X_train,X_validation,Y_train,Y_validation = train_test_split(X,Y,test_size=validation_size,
#     random_state=seed)

# 算法审查
# models = {}
# models['LR'] = LogisticRegression()
# models['LDA'] = LinearDiscriminantAnalysis()
# models['KNN'] = KNeighborsClassifier()
# models['CART'] = DecisionTreeClassifier()
# models['NB'] = GaussianNB()
# models['SVM'] = SVC()
# 评估算法
# results = []
# for key in models:
#     kfold = KFold(n_splits=10,random_state=seed,shuffle=True)
#     cv_results = cross_val_score(models[key],X_train,Y_train,cv=kfold,scoring='accuracy')
#     results.append(cv_results)
#     print('%s:%f(%f)' %(key,cv_results.mean(),cv_results.std()))

# 箱线图比较算法
# fig = pyplot.figure()
# fig.suptitle('Algorithm Comparison')
# ax = fig.add_subplot(111)
# pyplot.boxplot(results)
# ax.set_xticklabels(models.keys())
# pyplot.show()