# In this assignment, Prediction of survived column is done after Feature Engineering
# like Finding missing values, replace male and female with 1 and 2 resp, NaN values in Age is replaced
# with mode of the Age column and correlation between the columns are also treated.
# Based on the data, decision tree model with nosplit, split and model after applying GridSearchCV is created
# and their scores are presented
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import tree

data = pd.read_csv("https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv")
datap = data.copy()
datap= datap.drop(['PassengerId','Name','Ticket','Cabin','Embarked'],axis = 1)


def null_val(dat):
    null = dat.isnull()
    nulldes = pd.DataFrame(null.describe())
    collist = (nulldes.columns)
    print(len(collist))
    nullresf = []
    for i in range(len(collist)):
        if not (nulldes[collist[i]]['top']):
            print("No null values in column", collist[i])
        else:
            print(" Null values in column", collist[i])

    dat['Sex'].replace('female', 2, inplace=True)
    dat['Sex'].replace('male', 1, inplace=True)

    modage = int(dat['Age'].mode())
    print(modage)
    dat['Age'] = dat['Age'].fillna(modage)

    dat1 = dat.copy()
    dat1 =dat1.drop(['Survived'], axis = 1)
    datcorr = dat1.corr(method='pearson')
    datcorr.replace(1,0,inplace=True)
    datcorr = abs(datcorr)
    maxval = datcorr.max()
    maxvalind = datcorr.idxmax()
    af=[]
    bf =[]
    col = dat1.columns
    for i in range(len(maxval)):
        a = maxval[i]
        af.append(a)
        b = maxvalind[i]
        bf.append(b)
    corr1 = {'col1':col,'col2':bf, 'col3':af}
    corr1 = pd.DataFrame(corr1)
    for i in range(len(corr1)):
        if corr1['col3'][i]>0.89:
            d = (corr1.col3 == corr1['col3'][i]).sum()
            e =corr1['col2'][i]
            if d>1:
                corr1.drop([i], inplace=True)
                dat.drop([e],axis=1,inplace=True)
# Feature Engineering
null_val(datap)

print(datap.head(10))
def create(datm):
    X = datm.drop(['Survived'],axis =1)
    Y = datm['Survived']
    model1 = tree.DecisionTreeClassifier()
    model1.fit(X,Y)
    Acc1 = model1.score(X, Y)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,random_state=12)
    model2 = tree.DecisionTreeClassifier()
    model2.fit(x_train, y_train)
    Acc2 = model2.score(x_train, y_train)
    Acc2t = model2.score(x_test, y_test)

    gridParam = {'criterion':['gini','entropy'],
                 'max_depth':range(2,10,1),
                 'min_samples_split':range(2,10,1),
                 'splitter':['best','random']}
    model3 = GridSearchCV(estimator = model2,param_grid = gridParam,cv=5)
    model3.fit(x_train,y_train)
    Acc3 = model3.score(x_train,y_train)
    Acc3t = model3.score(x_test, y_test)
    return Acc1, Acc2, Acc2t, Acc3, Acc3t


# Model creation
score1,score2,score2t, score3, score3t =create(datap)
print('Score1 with out split',score1)
print('Score2 with split(train)',score2)
print('Score2 with split(test)',score2t)
print('Score3 with split(train)',score3)
print('Score3 with split(train)',score3t)
