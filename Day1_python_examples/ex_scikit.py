
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split, cross_val_score

iris = datasets.load_iris()

Xtrain, Xtest, ytrain, ytest = \
    train_test_split(iris.data, iris.target, test_size=0.4, random_state=True)


svc = svm.SVC(kernel='linear', C=1.0, probability=True)
svc.fit(Xtrain, ytrain)

score = svc.score(Xtest, ytest)
print("test score: ", score)

accuracy = cross_val_score(svc, iris.data, iris.target, cv=5)
print("Cross-validation: ", accuracy)

# source: https://github.com/krother/Python3_Module_Examples/blob/master/data_analysis/machine_learning/example_sklearn.py
