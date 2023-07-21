import pandas as pd      # Gerekli kütüphaneler import edilir.
import matplotlib.pyplot as plt
import numpy as np

# Veri Seti içeriye aktarılır, veriler ";" ile ayrılır.
df = pd.read_csv("Polynominal Linear Regression.csv", sep=";")


# Veri setindeki araba fiyat ve hız sütunlarını kullanarak bağımlı ve bağımsız değişkenleri belirliyoruz.
y = df.Araba_Max_Hiz.values.reshape(-1,1)
x = df.Araba_Fiyat.values.reshape(-1,1)


# Verileri dağılım grafiği ile görselleştiriyoruz.
plt.scatter(x, y)
plt.xlabel("Araba_Fiyat.values")
plt.ylabel("Araba_Max_Hiz.values")
plt.show()


#linear regression, y = b0 + b1*x
#multiple linear regression, y = b0 + b1*x1 + b2*x2


#Sklearn kütüphanesini kullanarak doğrusal regresyon modelini eğitiyoruz.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x,y)

#%% Predict

# Tahmin yaparak linear regression modelini görselleştiriyoruz.
y_head = lr.predict(x)

plt.plot(x,y_head,color="red", label="Linear" )
plt.show()

#10 milyon tl değerindeki arabanın hızı: 871km, bu veri saçmadır. çünkü hiçbir araç o  hızlara çıkamaz bu yüzden polynomial linear regression modelini kullanmamız gerek.
print("10 milyon tl lik araba hizi tahmini: ", lr.predict(np.array(10000).reshape(-1,1)))



#%% polynomial Linear regression
# polynomial Linear regression,  y = b0 + b1*x + b2*x^2 + b3*x^3 + bn*x^n

from sklearn.preprocessing import PolynomialFeatures     #kütüphane import edilir
polynomial_regression = PolynomialFeatures(degree = 4)   #4. dereceden bir polinom kullanarak modelimizi eğiticez.
x_polynomial = polynomial_regression.fit_transform(x)    #x yani fiyat bilgilerini modele yerleştiriyoruz.

#%%
linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial,y)   #polinomial modeli eğitiyoruz

#%%
y_head2 = linear_regression2.predict(x_polynomial)   #modelin tahmin sonuçlarını elde ediyoruz.

plt.plot(x,y_head2,color="green",label="polynomial")   #son olarak elde edilen tahmin sonuçlarını görselleştir.
plt.legend() 
plt.show()














