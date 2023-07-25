import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Random Forest regression dataset.csv",sep=";",header=None)

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

#örnek bir tahminde bulunuyoruz
print("7.8 seviyesinde fiyatın ne kadar olduğu: ",rf.predict([[7.8]]))

#x verilerinin minimum ve maksimum değerleri arasında 0.01 aralıklarla bir x_ dizisi oluşturuyoruz.
#bu diziyi kullanarak çizgiyi çizeceğiz.
x_ = np.arange(min(x), max(x), 0.01).reshape(-1,1)

#oluşturulan rf modelini kullanarak x_ dizisi üzerinde tahmin yapar ve sonuçlarını y_head içerisine aktarır.
y_head = rf.predict(x_)


#%% visualize - görselleştirme
plt.scatter(x,y,color="red")
plt.plot(x_, y_head, color="green")
plt.xlabel("Tribun level")
plt.ylabel("Price")
plt.show()






















