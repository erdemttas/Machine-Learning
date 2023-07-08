#Gerekli kütüphaneler import edilir.
import pandas as pd
import matplotlib.pyplot as plt



#Verileri içeren CSV dosyasını okuyoruz.
df = pd.read_csv("Linear_Regression_dataset.csv",sep=";")


#Verileri grafik üstünde gösteriyoruz
plt.scatter(df.deneyim,df.maas)
plt.xlabel("Deneyim")
plt.ylabel("maas")
plt.show()



#sklearn kütüphanesinin içinde machine learning algortimaları ve modeller vardır.
from sklearn.linear_model import LinearRegression

#linear regression modeli oluşturuyoruz.
linear_reg = LinearRegression()

#deneyim verilerini x değişkenine, maaş verilerini y değişkenine atıyoruz.
x = df.deneyim.values.reshape(-1,1)
y = df.maas.values  

#Modeli eğitiyoruz.
linear_reg.fit(x,y)

#%% prediction

#Tahmin yapmadan önce modelin katsayılarını belirliyoruz. b0 aşşağıdaki gibi iki farklı şekilde bulunabilir.
#predict() yöntemi, verilen girdi değerleri için tahmin yapar.
b0 = linear_reg.predict([[0]])
print("b0: ",b0)

#intercept_ özelliği y ekseninin kesme noktasını verir.
b0_ = linear_reg.intercept_
print("b0: ",b0)

#coef_ özelliği ise eğim (b1) değerini verir
b1 = linear_reg.coef_
print("b1: ",b1)


#maas = 1416 + 1162*deneyim

maas_yeni = 1416 + 1162*11
print(maas_yeni)

#100 yıl deneyimli birisinin maaşını tahmin ettik. Maaş = 117681.22598793.
print(linear_reg.predict([[100]]))







