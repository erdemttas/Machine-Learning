# <h1 align="center">Machine Learning Notes <br>(python kodları yorum satırı şeklinde açıklanmıştır)</h1>
<br><br>
# 1-Linear Regression
* line çizerken ki temel amaç data pointlere en yakın yerden geçmektir.
 <br>
 
![Çalışma Notu 1](https://github.com/erdemttas/Machine-Learning/assets/100941281/6ecb3086-2251-4310-8b90-5b7dfb343158)
<br>
- Line(kırmızı çizgi) data pointlerin y_head(predict) değerine uzaklığının karesinin alınıp toplanması sonucunda elde edilen değerin sample sayısına bölünmesi ile optimum line çizilir.
- y - y_head işlemi yapıldığında, kimi yerde (+) kimi yerde (-) değer sonucuna ulaşılır, eğer bu şekilde veriler toplanırsa artılar eksileri götürür ve 0 sonucuna ulaşılır. Bu iyi bir şey ama bizim modelimizde hatalar bulunmakta bu nedenle kare alma işlemi yaparız. En son elde ettiğimiz değer MSE(mean square error) ‘ dır, bu değere göre line çizilir.
- Temel Amacımız MSE’yi küçük tutmaktır, MSE küçük olursa çizgimiz(line) data pointlerin yakınından geçer.

![Çalışma Notu 2](https://github.com/erdemttas/Machine-Learning/assets/100941281/0cfa5607-483a-4a11-8bb3-914e289f58c9)

<br><br><br><br>

# 2-Multiple Linear Regression
- Multiple Linear Regression
   Linear regression ile Multiple linear regression aynı şeydir tek fark multiple linear regression birden fazla feature’a sahiptir.
Bir tane bağımlı değişken ve birden fazla bağımsız değişkenden oluşan modeldir.<br>
bağımlı değişken = maaş <br>
bağımsız değişken = deneyim, yaş
![Ekran görüntüsü 2023-07-18 190433](https://github.com/erdemttas/Machine-Learning/assets/100941281/456f2bd7-135c-4385-bea3-33f20156b89a)

<br><br><br><br>

# 3-Polynomial Linear Regression
- Polynomial Linear Regression
    
    Lineer regresyon, bir bağımlı değişken ile bir veya daha fazla bağımsız değişken arasındaki ilişkiyi ifade eden doğrusal bir model oluşturur. Ancak bazen verilerin doğrusal bir modelle 
    açıklanamayacak kadar karmaşık bir yapıya sahip olabileceği durumlar vardır. İşte bu noktada polinomal lineer regresyon devreye girer.
    
    Polinomal lineer regresyon, doğrusal olmayan veri kümelerini modellemek için polinomları kullanır. Temelde, bir polinom fonksiyonu kullanılarak bağımlı değişkenin polinom derecesine        göre 
    bağımsız değişkenlere en uygun şekilde bağlanmaya çalışılır. Polinom derecesi, modelin karmaşıklığına bağlı olarak seçilir.
    
    Örneğin, basit bir polinomal lineer regresyon modeli şu şekilde ifade edilebilir:
    
    y = b0 + b1*x + b2*x^2 + ... + bn*x^n
  ![Ekran görüntüsü 2023-07-21 090141](https://github.com/erdemttas/Machine-Learning/assets/100941281/7f3b67e4-2320-41cb-9b0b-b6d8ce2475f7)
![img](https://github.com/erdemttas/Machine-Learning/assets/100941281/c35f8045-aa61-4bac-ab52-329911f40433)

<br><br><br><br> 

# 4-Decision Tree Regression
- Decision Tree Regression
    
    Karar ağacı, adından da anlaşılacağı gibi bir ağaç yapısını takip eder. Ağacın en üstünde "kök düğüm" bulunur ve veri kümesini bölme kriterini belirler. Kök düğümden itibaren, her düğüm veri kümesini bir özelliğe göre iki veya daha fazla alt kümeye böler. Bölmeler, veri kümesindeki özniteliklerin değerlerine göre gerçekleşir ve böylece farklı alt kümeler oluşturulur.
    
    Karar ağacı oluştururken, bölmelerin en iyi şekilde yapılması için veri kümesini bölme kriterleri değerlendirilir. En iyi bölme, verileri mümkün olduğunca homojen alt kümeler halinde bölen ve böylece her alt kümedeki verilerin benzer nitelikte olmasını sağlayan bir kriterdir.
    
    Regresyon problemleri için, karar ağacı düğümlerinde her alt kümeye ait verilerin ortalama değeri hesaplanır. Böylece, alt kümelerdeki verilere dayalı olarak regresyon modeli oluşturulur.
    
    Decision Tree Regression'ın avantajları şunlardır:
    
    - Veri kümesinin doğrusal olmayan yapılarını ve kesişen eğrileri yakalayabilir.
    - Çok sayıda özelliği işlemek için etkilidir ve boyut indirgeme gibi ek ön işleme adımlarına ihtiyaç duymaz.
    - Yorumlanması kolaydır, çünkü karar ağacı aşamaları basit kararlar olarak açıklanabilir.
    
    Ancak, karar ağaçları aşırı karmaşık hale gelebilir ve aşırı uydurmayı (overfitting) teşvik edebilirler. Bu nedenle, ağacın derinliğini veya bölme kriterlerini düzenlemek gibi modelin aşırı uyumu önlemek için önlemler alınmalıdır. Ayrıca, bazı durumlarda karar ağaçları, veri kümesindeki küçük değişikliklere oldukça duyarlı olabilir. <br><br>

    - Elimizde iki tane feature var bunlar x1 ve x2 dir. bu değerler y değerini predict etmemizi sağlar.
    - Splitler information entropye göre belirlenir.
    - Split işlemleri gerçekleştirildikten sonra kök düğümden başlayarak büyüklük küçüklük  durumuna göre leaf(yaprak) bölgelerinin ortalamalarını alıyoruz. bu şeklide bir ağaç yapısı oluşuyor ve en sonunda yeni predict değerimizi bu ağaç yapısına göre buluyoruz. Kısaca leaf bölgesinin ortalama değeri bizim predict ettiğimiz değer oluyor.

![ekran goruntusu](https://github.com/erdemttas/Machine-Learning/assets/100941281/41bfa1d4-5c8c-4f5d-ace0-24257dbadef8)
<br>
* örnek olarak: tribün seviyesi 2.5 ile 3.5 arası olan kişiler 75 tl vermiştir.<br>
3.6 ve sonrasında bir anda fiyat 70 tl olmuştur ve gene belirli bir aralık boyunca fiyat sabit kalacaktır.<br> Kısaca belirli aralıktaki veriler, içerisinde bulundukları leaf’lerin belirli aralık boyunca ortalama değerlerini alırlar.<br>
![Ekran görüntüsü 2023-07-06 133309](https://github.com/erdemttas/Machine-Learning/assets/100941281/705b8b96-17b5-43d5-a7b8-b23ef2f02b39)
<br><br><br><br>

# 5-Random Forest Regression
Random forest, ensemble learning üyesidir. ensemble learning aynı anda pek çok algoritmayı kullanarak elde edilen bir modeldir.

Random forest, ağaçların toplamından oluşan bir yapıdır. Decision tree ler belirlenen ölçüde toplanıyor ve çıkan sonuçların ortalaması alınarak random forest değeri elde ediliyor. Bu algoritmalar çok güçlü algoritmalardır çünkü bir çok farklı algoritmayı birleştiriyorlar.

Random forest da genellikle recommendation systemlerde falan kullanılır, örneğin bir film izlendiğinde benzer diğer filmlerin önerilmesi gibi.

Bir datamız var, bu datanın içerisinden n sayıda random sample seçilir ve subdata elde edilir. sonrasında subdatayı tree ler ile eğitiyoruz , eğitim sonunda tree’lerdeki değerler toplayıp ortalamayı alıyoruz ve sonucu elde ediyoruz ve model oluşuyor. sonra tekrar tekrar başa dönüp bu işlemleri tekrarlıyoruz. bu şekilde model güçlenmiş oluyor.

Decision tree deki gibi bir grafik çıktı ve aynı mantıkla çalışıyor. Random forestin decision treeden farkı 1 tane decision tree kullanmak yerine 100 tane decision tree kullanıldı. 

100 tane decision tree 1 tane decision treeden iyidir. yani random forest algoritması decision tree algoritmasından daha iyi sonuçlar verir.

randon_state, her seferinde aynı bölünme oranının geçekleşmesini sağlıyor. Alacağı parametrenin çok da bir önemi yoktur.

![Ekran görüntüsü 2023-07-06 140833](https://github.com/erdemttas/Machine-Learning/assets/100941281/e992fd05-d470-4fe9-ac45-1eda4f5129ad)
![Ekran görüntüsü 2023-07-06 134447](https://github.com/erdemttas/Machine-Learning/assets/100941281/96b7d9b6-a944-4b5f-9eee-ba754d8b65c9)


<br><br><br><br>
# 6-Evaluation Regression Models
- Evaluation Regression Models
    
    Evaluation modeli, bir sistemin, ürünün, hizmetin veya projenin etkinliğini ve başarısını ölçmek ve değerlendirmek için kullanılan bir yapı veya yöntemdir. Bu tür modeller, performansı niceliksel veya niteliksel olarak değerlendirebilir ve geliştirmeye odaklanabilir.

![Evaluation Regression Model](https://github.com/erdemttas/Machine-Learning/assets/100941281/c3f08517-7d0e-436e-ba64-bc5cd168a110)


