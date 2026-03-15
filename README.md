#MLE ile Akıllı Şehir Planlaması Trafik Yoğunluk Analizi
Bu proje, YZM212 Makine Öğrenmesi dersi 2. laboratuvar ödevi kapsamında hazırlanmıştır. Projede, bir caddeden geçen araç sayısının Poisson Dağılımı kullanılarak modellenmesi ve en uygun yoğunluk parametresinin lambda Maksimum Olabilirlik Kestirimi (MLE) yöntemiyle hesaplanması hedeflenmektedir. 
#Problem Tanımı 
Şehir planlama süreçlerinde trafik yoğunluğunu doğru tahmin etmek hayati önem taşır. Bu çalışmada, bir dakikada geçen araç sayıları üzerinden aşağıdaki sorulara yanıt aranmıştır:
Gözlemlenen veriler ışığında en olası trafik yoğunluk parametresi lambda nedir? Teorik çözümler ile sayısal kodlama sonuçları birbiriyle örtüşmekte midir? Model, gerçek verilerle ne kadar uyumludur? 
#Veri Seti 
Çalışmada kullanılan trafik verisi, bir dakikalık aralıklarla yapılan 14 farklı gözlemden oluşmaktadır: 
[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15] 
#Yöntem 
  Analitik Çözüm: Poisson olasılık fonksiyonu kullanılarak Likelihood ve Log-Likelihood fonksiyonları türetilmiştir. Fonksiyonun türevi alınarak hat{lambda}MLE değerinin verilerin aritmetik ortalamasına eşit olduğu kanıtlanmıştır. 
  Sayısal Optimizasyon: Python'da scipy.optimize kütüphanesi kullanılarak Negatif Log-Olabilirlik (NLL) fonksiyonu minimize edilmiş ve sayısal olarak en iyi parametre bulunmuştur.     
  Görselleştirme: Elde edilen model ile gerçek verilerin histogramı karşılaştırılarak modelin başarısı görselleştirilmiştir. 
#Sonuçlar ve Yorumlar 
  Analitik ve Sayısal Uyum: Yapılan hesaplamalar sonucunda aritmetik ortalama ile optimizasyon çıktısının birbirine tam uyum sağladığı görülmüştür. 
    Aykırı Değer Etkisi: MLE yönteminin uç değerlere karşı hassas olduğu saptanmıştır. Veri setine eklenecek hatalı bir "200" gözlemi, ortalamayı yukarı çekerek belediyenin yanlış ( kararlar almasına sebebiyet verebilir.
