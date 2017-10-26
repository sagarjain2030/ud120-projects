#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

t0 = time()
clf = svm.SVC(kernel='rbf',C=10000)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train,labels_train)
print('time required ' , time() - t0 , '  sec')
t1 = time()
print(clf.score(features_test,labels_test))
print('time required ' , time() - t1 , '  sec')
print("Done")
#########################################################
### your code goes here ###

#########################################################
pred = clf.predict(features_test)

print '10 =  ',pred[10]
print '26 =  ',pred[26]
print '50 =  ',pred[50]

x = [s for s in pred if s==1]
print(len(x))