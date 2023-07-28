# <h1 align="center">Machine Learning Notes <br>(python kodları yorum satırı şeklinde açıklanmıştır)</h1>
<br><br>
# 1-Linear Regression
- Lineer regresyon, bağımlı bir değişken ile bir veya daha fazla bağımsız değişken arasındaki doğrusal ilişkiyi ifade eden bir denklem oluşturur.
  özellikle niceliksel verilerde ve özellikler arasında doğrusal bir ilişki olduğu durumlarda etkili bir modelleme tekniğidir.<br> Örneğin, deneyim maaş ilişkisi <br>
  Temeldeki amaç MSE(HATA KARELERİ ORTALAMASI) bu değeri minimum yapmaktır.
![Çalışma Notu 1](https://github.com/erdemttas/Machine-Learning/assets/100941281/6ecb3086-2251-4310-8b90-5b7dfb343158)
![Çalışma Notu 2](https://github.com/erdemttas/Machine-Learning/assets/100941281/0cfa5607-483a-4a11-8bb3-914e289f58c9)

<br><br><br><br>

# 2-Multiple Linear Regression
- Multiple Linear Regression
    Bir bağımlı değişken bir veya daha fazla bağımsız değişkenden oluşan bir yapıdır.
    Bu yapının amacı bağımlı ve bağımsız değişkenler arasındaki  ilişkiyi modellemek için kullanılır.
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

![Ekran görüntüsü 2023-07-06 133309](https://github.com/erdemttas/Machine-Learning/assets/100941281/705b8b96-17b5-43d5-a7b8-b23ef2f02b39)


<br><br><br><br>





