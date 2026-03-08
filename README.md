HMM-Speech-Recognition
Bu proje, YZM212 Makine Öğrenmesi Dersi kapsamında Gizli Markov Modelleri (HMM) kullanılarak izole kelime tanıma sisteminin (Speech Classifier) temel bir simülasyonunu içermektedir.

Problem Tanımı ve Yöntem
Ses verilerindeki fonemler HMM deki gizli durumlar  olarak modellenmiş, ses spektrumu özellikleri (High/Low frekans) ise gözlemler  olarak ele alınmıştır.
Viterbi algoritması el ile hesaplanarak en olası durum dizilimi bulunmuş ve `hmmlearn` kütüphanesi ile log-likelihood skorlaması yapılarak kelime sınıflandırması gerçekleştirilmiştir.

Analiz ve Yorumlama
1. Ses verisindeki gürültü, HMM modelindeki Emisyon Olasılıklarını nasıl etkiler?
Gürültü, emisyon  olasılıklarının dağılımını düzleştirir ve belirli bir fonem ile spesifik bir akustik gözlem arasındaki güçlü bağı zayıflatır. 
Gürültülü ortamlarda model, bir durumu diğerinden ayırmakta zorlanır çünkü belirsizlik artar.

2. Gerçek bir sistemde binlerce kelime olduğunu düşünürsek, Viterbi yerine neden daha karmaşık yapılar (Deep Learning gibi) tercih edilmeye başlanmıştır?
HMM ler Markov varsayımına dayanır. Yani bir durum sadece kendinden bir önceki duruma bağlıdır. Konuşma dili ise uzun vadeli bağlamsal bağımlılıklar içerir. 
Kelime dağarcığı binlere çıktığında, HMM lerin durumu uzayı (state space) yönetilemez hale gelir. 
Derin Öğrenme (RNN, LSTM, Transformer modelleri) ise akustik özellikleri manuel olarak tanımlamaya gerek kalmadan veriden hiyerarşik olarak öğrenebilir ve geniş bağlamı çok daha yüksek doğrulukla yakalayabilir.

Kurulum ve Çalıştırma
Projeyi çalıştırmak için gerekli kütüphaneleri yükleyin:
`pip install -r requirements.txt`

Kodu çalıştırmak için:
`python src/recognizer.py`