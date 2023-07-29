import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("5-Random Forest regression dataset.csv",sep=";",header=None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)


#%%
from sklearn.ensemble import RandomForestRegressor

#RandomForestRegressor sınıfından bir rf modeli oluşturuyoruz.
#n_estimators ile 100 ağaçtan oluşan bir orman kullanacağımızı belirtiriz.
#random_state ise modelin her seferinde aynı sonucu üretmesini sağlayan başlangıç durumunu ifade eder.
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)

#rf modelini x ve y verileri üzerinde eğitiyoruz. model x verilerini girdi y verilerini hedef olarak algılar.
rf.fit(x,y)

y_head = rf.predict(x)

#%% Evaluation Regression Model

from sklearn.metrics import r2_score

print("r_score: ", r2_score(y, y_head))





















