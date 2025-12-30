# 🎲 LCG Rastgele Sayı Üreteci

**Linear Congruential Generator (LCG)** algoritması kullanılarak geliştirilmiş bir rastgele sayı üreteci projesi.

## 📚 Proje Hakkında

Bu proje, kriptografi ve istatistik derslerinde yaygın olarak öğretilen **Linear Congruential Generator (LCG)** algoritmasının Python implementasyonudur. LCG, en yaygın kullanılan pseudo-random number generator algoritmalarından biridir.

### 🧮 LCG Algoritması

LCG aşağıdaki matematiksel formülü kullanır:

```
X(n+1) = (a × X(n) + c) mod m
```

**Parametreler:**
- **m** (Modulus): 2³² = 4,294,967,296
- **a** (Çarpan): 1,664,525 (Park & Miller'ın önerisi)
- **c** (Artış): 1,013,904,223 (Numerical Recipes)
- **X₀** (Seed): Başlangıç değeri

## 🚀 Özellikler

✅ **Sıfırdan yazılmış LCG algoritması**  
✅ **Çoklu rastgele sayı fonksiyonları** (random, randint, choice, shuffle, sample)  
✅ **İstatistiksel analiz araçları** (Dağılım analizi, Chi-Square testi)  
✅ **Görselleştirmeler** (Histogram, 2D/3D scatter plot)  
✅ **8 farklı kullanım örneği**  
✅ **Detaylı dokümantasyon**

## 📁 Dosya Yapısı

```
RASTGELE SAYI/
│
├── random_generator.py    # Ana LCG algoritması
├── visualize.py          # İstatistiksel analiz ve görselleştirme
├── examples.py           # 8 farklı kullanım örneği
├── requirements.txt      # Gerekli kütüphaneler
├── README.md            # Bu dosya
└── .gitignore           # Git ignore dosyası
```

## 🛠️ Kurulum

### 1. Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

### 2. Temel Kullanım

```python
from random_generator import LCGRandomGenerator

# Üreteci başlat
rng = LCGRandomGenerator(seed=42)

# 0-1 arası rastgele sayı
print(rng.random())  # Örnek: 0.654321

# Belirli aralıkta tam sayı
print(rng.randint(1, 100))  # Örnek: 73

# Listeden rastgele seçim
fruits = ["Elma", "Armut", "Muz"]
print(rng.choice(fruits))  # Örnek: "Muz"
```

## 📊 Çalıştırma

### Ana Algoritma Testi

```bash
python random_generator.py
```

### İstatistiksel Analiz ve Görselleştirme

```bash
python visualize.py
```

Bu komut aşağıdaki dosyaları oluşturur:
- `histogram.png` - Dağılım histogramı
- `scatter_2d.png` - 2D korelasyon grafiği
- `scatter_3d.png` - 3D korelasyon grafiği

### Kullanım Örnekleri

```bash
python examples.py
```

Bu komut 8 farklı örnek senaryoyu çalıştırır:
1. ✅ Temel kullanım
2. 🎲 Zar atma simülasyonu
3. 🎰 Piyango numarası üretme
4. 🔐 Rastgele şifre oluşturma
5. 🥧 Monte Carlo ile Pi tahmini
6. 🃏 Kart destesi karıştırma
7. ⚖️ Ağırlıklı rastgele seçim
8. 🚶 Rastgele yürüyüş simülasyonu

## 📈 API Referansı

### `LCGRandomGenerator` Sınıfı

#### `__init__(seed=None)`
Üreticiyi başlatır. Seed verilmezse sistem zamanı kullanılır.

#### `random() -> float`
0.0 ile 1.0 arasında rastgele ondalık sayı döndürür.

#### `randint(a, b) -> int`
a ile b arasında (ikisi de dahil) rastgele tam sayı döndürür.

#### `choice(sequence) -> any`
Verilen listeden rastgele bir eleman seçer.

#### `shuffle(items) -> list`
Listeyi Fisher-Yates algoritması ile karıştırır.

#### `sample(population, k) -> list`
Popülasyondan k adet benzersiz rastgele örnek seçer.

#### `reset(seed=None)`
Üreteciyi yeniden başlatır.

#### `get_state() -> dict`
Üretecin mevcut durumunu döndürür.

## 🧪 İstatistiksel Testler

Proje, üretilen sayıların kalitesini değerlendirmek için şu testleri içerir:

1. **Dağılım Analizi**: Ortalama, standart sapma, min/max değerler
2. **Chi-Square Testi**: Uniform dağılım kontrolü
3. **Korelasyon Analizi**: 2D ve 3D scatter plot'lar ile görsel inceleme

## 📸 Örnek Çıktılar

### Histogram
![Histogram Örneği](histogram.png)

### 2D Korelasyon
![2D Scatter Örneği](scatter_2d.png)

### 3D Korelasyon
![3D Scatter Örneği](scatter_3d.png)

## 🎯 Kullanım Senaryoları

- 🎲 Oyun geliştirme (zar, kart oyunları)
- 🔐 Güvenli olmayan şifre/token üretimi
- 📊 Monte Carlo simülasyonları
- 🧪 Eğitim ve öğretim amaçlı
- 🎰 Piyango ve rastgele seçim sistemleri

## ⚠️ Önemli Notlar

> [!WARNING]
> **Kriptografik Amaçlar İçin Kullanmayin!**  
> LCG algoritması deterministiktir ve tahmin edilebilirdir. Güvenlik gerektiren uygulamalar için (şifreleme, güvenli token üretimi vb.) `secrets` modülünü kullanın.

> [!NOTE]
> **Eğitim Amaçlı**  
> Bu proje, rastgele sayı üretimi algoritmalarını öğretmek için tasarlanmıştır. Üretim ortamında Python'un yerleşik `random` modülünü kullanmanız önerilir.

## 📚 Referanslar

- [Wikipedia - Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator)
- Numerical Recipes in C (Press, Teukolsky, Vetterling, Flannery)
- Park, S. K., & Miller, K. W. (1988). Random Number Generators: Good Ones Are Hard To Find

## 👤 Yazar

**Suzan**  
Beyza Hoca - Kriptografi Dersi Projesi

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir ve serbestçe kullanılabilir.

---

⭐ **Beğendiyseniz yıldız vermeyi unutmayın!**
