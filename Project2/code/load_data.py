#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import random 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import sys

def load_data():

    mushrooms= pd.read_csv('D:\学习相关\专业英语\datasets_478_974_mushrooms.csv')


    X=mushrooms.drop('class',axis=1) #去掉class这一列，得到输入的22个特征

    y=mushrooms['class'] #得到class标签


    Encoder_X = LabelEncoder() #字母转换为数字

    for col in X.columns:
        X[col] = Encoder_X.fit_transform(X[col])
    

    X=np.array(X)


    Encoder_y=LabelEncoder()

    y = Encoder_y.fit_transform(y)
    return X,y


def vectorized_result(j):
    e = np.zeros((2, 1))
    e[j] = 1.0
    return e

#调整格式，使得数据变成向量形式，输入层有22个神经元
def adjust_data(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=0 )#分类
    #对训练集调整
    
    train_in = np.array([x[0:] for x in X_train]).astype('float')#转换成浮点类型
    train_vect=[np.reshape(x, (22,1)) for x in train_in]#变成向量形式
    train_out = [vectorized_result(y) for y in y_train]

    #测试集同理
    test_in=np.array([x[0:] for x in X_test]).astype('float')
    test_vect=[np.reshape(x, (22,1)) for x in test_in]
    test_out = [vectorized_result(y) for y in y_test]

    train_datasets = list(zip(train_vect, train_out))
    test_datasets = list(zip(test_vect, test_out))
    
    return train_datasets,test_datasets



