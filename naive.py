import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report 
from sklearn.metrics import accuracy_score
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from MLFunctions import k_fold_cross_validation
archivo=sio.loadmat('EEG_Data')
X=archivo['X']
Y=archivo['Y']
m,n = X.shape
Y = Y.reshape((m,1))
k = 10
Y=Y.reshape((m,1))
Fold_Index = k_fold_cross_validation(k,m)
C=np.linspace(0.01,10,5) # C
G=np.linspace(0.01,10,5) # Gamma
degrees = [0, 1, 2, 3, 4, 5, 6]
coef0=[0,1]
BestAcc=0
BestGamma=0
BestC=0
n_neighbors=3
for i in range(k):
    Xtest = X[Fold_Index == i,:]
    Ytest = Y[Fold_Index == i,:]
    Xtrain = X[Fold_Index != i,:]
    Ytrain = Y[Fold_Index != i,:]
    Model = GaussianNB()
    Model.fit(Xtrain,Ytrain)
    Y_es = Model.predict(Xtest)
    Y_es = np.expand_dims(Y_es,axis=1)
    Vn,Fp,Fn,Vp = confusion_matrix(Ytest,Y_es).ravel()    
    AccActual = accuracy_score(Ytest,Y_es)
    if AccActual > BestAcc:
        BestAcc = AccActual
print("KNN su Accuracy " + str(BestAcc))
print(classification_report(Ytest,Y_es))

