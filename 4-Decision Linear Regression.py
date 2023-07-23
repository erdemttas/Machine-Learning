import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Excel csv dosyasını alıyoruz, ; ile seperate ediyoruz, tablonun üstündeki değerler başlık olarak okunduysa header=None diyoruz.
df = pd.read_csv("Decision tree regression.csv", sep=";", header=None)

#iloc pandas dataframelerinde indeksleme yapmak için kullanılır, örnek tüm satıları al, sütunlardan 0. sütunu al
#values seçilen sütunun değerlerini bir numpy dizisi olarak alır.
#reshape ise (10,) ndan (10,1) yapmak için kullanılır. sklearn için gereklidir bu işlem
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)



#%% Decision tree regression 
from sklearn.tree import DecisionTreeRegressor

#DecisionTreeRegressor sınıfından bir model oluşturuyoruz
tree_reg = DecisionTreeRegressor()

#tree_reg modelini x ve y verileri üzerinde eğitiyoruz, x verileri girdi y verileri hedef olarak kullanılarak model eğtilir.
tree_reg.fit(x,y)

#model, örnek bir tahmin yapması için değer gireriz.
tree_reg.predict([[5.5]])

#minmum değerden max değere kadar 0.01 artarak x_grid dizisi oluşturulur.
x_grid = np.arange(min(x), max(x), 0.01).reshape(-1,1)

#oluşuturulan modeli kullanarak x verileri üzerinde tahmin yapar ve sonuçları y_head e aktarır.
y_head = tree_reg.predict(x_grid)


#%% visualize
plt.scatter(x, y, color="red")

plt.plot(x_grid, y_head, color = "green")
plt.xlabel("tribun level")
plt.ylabel("price")
plt.show()










