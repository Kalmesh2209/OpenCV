# -*- coding: utf-8 -*-
"""Dia_kalmesh_2905

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aothD5apCr909NjF0xvvz4bY5ynl-XeR
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,BatchNormalization
from sklearn.model_selection import train_test_split

data=pd.read_csv('/content/drive/My Drive/diabetes.csv')

data.head()

data.describe()

x=data.iloc[:,:-1]
y=data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

x_train.shape

y_train.shape

model=Sequential()

model.add(Dense(30,input_dim=8))
model.add(BatchNormalization())
model.add(Dense(100,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10,batch_size=10)

model.evaluate(x_test,y_test)