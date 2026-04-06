# Özdeğer ve Özvektörler – Ödev Raporu

**Ders:** YZM212 Makine Öğrenmesi  
**Laboratuvar:** III. Değerlendirme (29.03.2026)  
**Konu:** Matris Manipülasyonu, Özdeğer ve Özvektör Hesaplama

---

## Soru 1 – Makine Öğrenmesi ile Matris Manipülasyonu, Özdeğer ve Özvektörlerin İlişkisi

### Temel Tanımlar

**Matris Manipülasyonu**, matrisler üzerinde gerçekleştirilen toplama, çarpma, transpoz alma, ters matris bulma, ayrışım (decomposition) gibi matematiksel işlemlerin bütünüdür. Makine öğrenmesinde veriler çoğunlukla matris biçiminde temsil edildiğinden bu işlemler algoritmaların çekirdeğini oluşturur.

**Özdeğer (Eigenvalue)**, bir $A$ kare matrisi için $A \mathbf{v} = \lambda \mathbf{v}$ denklemini sağlayan $\lambda$ skaleridir. Bu denklem, $A$ dönüşümünün $\mathbf{v}$ vektörünü yalnızca ölçeklendirdiğini (yönünü değiştirmediğini) ifade eder.

**Özvektör (Eigenvector)**, yukarıdaki denklemdeki $\mathbf{v}$ sıfırdan farklı vektördür. Özvektörler, bir dönüşümün "değişmez eksenlerini" tanımlar.

### Makine Öğrenmesindeki Kullanım Alanları

#### 1. Temel Bileşen Analizi (PCA)
PCA, yüksek boyutlu veriyi daha az boyuta indirgerken bilgi kaybını minimize eden en yaygın boyut indirgeme tekniğidir. Kovaryans matrisinin özdeğer ayrışımı yapılarak en büyük özdeğerlere karşılık gelen özvektörler (temel bileşenler) bulunur. Bu özvektörler verinin en fazla varyans içerdiği yönleri gösterir.

#### 2. Tekil Değer Ayrışımı (SVD)
SVD, bir matrisi $A = U \Sigma V^T$ biçiminde üç faktöre ayırır. Önerici sistemler, görüntü sıkıştırma ve NLP'deki gizli anlamsal analiz (LSA) bu tekniği kullanır.

#### 3. Spektral Kümeleme (Spectral Clustering)
Graf Laplasyan matrisinin özdeğer ayrışımından elde edilen özvektörler, veri noktalarını kümelere ayırmak için kullanılır. K-means'ın başarısız olduğu karmaşık şekilli kümeleri tespit edebilir.

#### 4. Google PageRank
Web sayfaları arası geçiş matrisinin en büyük özdeğerine karşılık gelen özvektör, sayfaların sıralama skorlarını verir.

#### 5. Lineer Ayrımsal Analiz (LDA)
Sınıflar arası saçılım matrisi ile sınıf içi saçılım matrisinin genelleştirilmiş özdeğer problemi çözülerek sınıfları en iyi ayıran yönler bulunur.

### Referanslar

- Brownlee, J. (2019). *Introduction to Matrices and Matrix Arithmetic for Machine Learning*. MachineLearningMastery.com. https://machinelearningmastery.com/introduction-matrices-machine-learning/
- Brownlee, J. (2019). *Gentle Introduction to Eigenvalues and Eigenvectors for Machine Learning*. MachineLearningMastery.com. https://machinelearningmastery.com/introduction-to-eigendecomposition-eigenvalues-and-eigenvectors/
- Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge Press.

---

## Soru 2 – NumPy `linalg.eig` Fonksiyonu

### Dokümantasyon Özeti

`numpy.linalg.eig(a)` fonksiyonu, kare bir matrisin özdeğerlerini ve sağ özvektörlerini hesaplar.

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

**Parametreler:**
- `a`: `(..., M, M)` boyutlu kare ndarray

**Döndürür:**
- `eigenvalues`: `(..., M)` boyutlu ndarray – özdeğerler (karmaşık olabilir)
- `eigenvectors`: `(..., M, M)` boyutlu ndarray – her **sütun** bir normalize özvektör

**Önemli Notlar:**
- Simetrik matrisler için `eigh` daha kararlı ve verimlidir.
- Sonuçlar karmaşık sayı içerebilir; gerçek kısım için `.real` kullanılır.
- Döndürülen özvektörler normalize edilmiştir (`||v|| = 1`).

### Kaynak Kod Analizi

NumPy'ın `linalg.eig` uygulaması `numpy/linalg/linalg.py` dosyasında yer alır. İşleyiş şöyle özetlenebilir:

1. **Giriş doğrulama:** Matrisin kare ve sayısal olduğu kontrol edilir.
2. **LAPACK çağrısı:** Matris türüne göre `dgeev` (float64) veya `zgeev` (complex128) LAPACK rutini çağrılır.
3. **LAPACK `dgeev`** önce matrisi Hessenberg formuna dönüştürür, ardından QR iterasyonu ile özdeğerleri bulur.
4. Sonuçlar Python ndarray'e dönüştürülerek döndürülür.

Bu yaklaşım, doğrudan Python'da yazılmış QR algoritmasından çok daha hızlı ve sayısal olarak kararlıdır.

**Kaynak:** https://github.com/numpy/numpy/tree/main/numpy/linalg  
**Doküman:** https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html

---

## Soru 3 – Manuel QR Algoritması ile Karşılaştırma

### Uygulanan Yaklaşım

[LucasBN/Eigenvalues-and-Eigenvectors](https://github.com/LucasBN/Eigenvalues-and-Eigenvectors) deposu referans alınarak QR algoritması Python ile sıfırdan uygulanmıştır:

1. **Gram-Schmidt QR Ayrışımı:** Her iterasyonda $A_k = Q_k R_k$ ayrışımı Gram-Schmidt ortonormalizasyonu ile yapılır.
2. **Matris Güncelleme:** $A_{k+1} = R_k Q_k$ olarak güncellenir.
3. **Yakınsama:** Alt üçgen elemanların Frobenius normu eşik değerin ($10^{-9}$) altına düşünce durdurulur.
4. **Özdeğerler:** Yakınsayan matrisin köşegen elemanları özdeğerleri verir.
5. **Özvektörler:** Her $\lambda_i$ için $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$ sisteminin null-space'i SVD ile bulunur.

### Test Matrisi

$$A = \begin{pmatrix} 4 & -2 & 1 \\ 2 & 5 & -1 \\ -1 & 2 & 6 \end{pmatrix}$$

### Sonuçlar

| Yöntem | λ₁ | λ₂ | λ₃ |
|--------|----|----|----|
| QR (Manuel) | ~2.879 | ~5.000 | ~7.121 |
| NumPy `eig` | ~2.879 | ~5.000 | ~7.121 |
| Fark | < 10⁻⁸ | < 10⁻⁸ | < 10⁻⁸ |

İki yöntem pratikte özdeş sonuçlar üretmektedir.

### Kaynak

- LucasBN (2020). *Eigenvalues-and-Eigenvectors*. GitHub. https://github.com/LucasBN/Eigenvalues-and-Eigenvectors

---

## Dosya Yapısı

```
3. EigenVectorsValues/
├── EigenVectorsValues.ipynb   # Ana notebook (QR algoritması + NumPy karşılaştırması)
└── Readme.MD                  # Bu rapor
```

---

*Rapor, ödev gereklilikleri kapsamında hazırlanmıştır.*
