import pandas as pd     #Gerekli kütüphaneler import edilir.
import numpy as np
from sklearn.linear_model import LinearRegression

#verileri içeri aktarıyoruz. Ve ";" ile ayırıyoruz.
df = pd.read_csv("Multiple_Linear_Regression.csv", sep=";")

#x ekseni olarak gelen verilerin 1. ve 3. sütunlarını seçiyoruz. bu sütunlar deneyim ve yaştır. 
x = df.iloc[:,[0,2]].values

#y ekseni olarak maaş değerini alıyoruz.
y = df.maas.values.reshape(-1,1)

#%%

#model oluşturulur.
Multiple_Linear_Regression = LinearRegression()

#x ve y modele yerleştirilir. bu modelin eğitildiği anlamına gelir.
Multiple_Linear_Regression.fit(x,y)

# doğrunun y eksenini kesen kısımı, b0 bulunur.
print("b0: ",Multiple_Linear_Regression.intercept_)

# b1 ve b2 eğimler bulunur
print("b1,b2: ",Multiple_Linear_Regression.coef_)

# 35 yaşındaki iki kişinin 10 yıl deneyimli olanı 12879.934 tl kazanıyor.
# 5 yıl deneyimli olan kişi ise 7020.400 tl kazanıyor.
# bu şekilde tahmin işlemi gerçekleştirmiş olmaktayız.
Multiple_Linear_Regression.predict(np.array([[10,35],[5,35]]))















