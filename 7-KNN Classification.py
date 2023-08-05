import pandas as pd   # Gerekli kütüphaneler import edilir.
import matplotlib.pyplot as plt
import numpy as np

# %%   Excel Verisini içeri aktarma
data = pd.read_csv("data.csv")

# %% Gereksiz olan id ve Unnamed: 32 sütunlarını kaldırma
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

# %%  iyi ve kötü huylu tümörün görselleştirilmesi
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]
# scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha= 0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha= 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

# %% iyi ve kötü huylu tümör bilgisini (M/B) 0 VE 1 lere çeviriyoruz.
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values   # 0 ve 1 değerlerini tutuyor.
x_data = data.drop(["diagnosis"],axis=1)   #diagnosis(teşhis) haricindekileri tutuyor.

# %%
# KNN'de normalization önemlidir. normalizasyon olmazsa başarı 0.92 normalizasyon olursa başarı 0.96
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

#%% train test split / %30 test %70 train için ayırıyoruz.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)


#%% KNN Model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 10) # n_neigbors = k, kaç komşu olacağına karar verme.
knn.fit(x_train, y_train)   # modeli eğitme
prediction = knn.predict(x_test)   #tahminde bulunöa

print("{} NN Score: {}".format(10, knn.score(x_test, y_test)))   #10 komşulu olunca KNN score = 0.9649122807017544

#%% En iyi K değerini bulmak / en iyi k değeri 10 civarı 50 civarı vb. dir

score_list = []
for each in range(1,50):
    knn2 = KNeighborsClassifier(n_neighbors= each)
    knn2.fit(x_train, y_train)
    score_list.append(knn2.score(x_test, y_test))

plt.plot(range(1,50), score_list)
plt.xlabel("K values")
plt.ylabel("accuracy")
plt.show()








