# LCG Rastgele Sayi Ureteci

**Linear Congruential Generator (LCG)** algoritmasi kullanilarak gelistirilmis bir rastgele sayi ureteci projesi.

## Proje Hakkinda

Bu proje, kriptografi ve istatistik derslerinde yaygin olarak ogretilen **Linear Congruential Generator (LCG)** algoritmasinin Python implementasyonudur. LCG, en yaygin kullanilan pseudo-random number generator algoritmalarindan biridir.

### LCG Algoritmasi

LCG asagidaki matematiksel formulu kullanir:

```
X(n+1) = (a × X(n) + c) mod m
```

**Parametreler:**
- **m** (Modulus): 2^32 = 4,294,967,296
- **a** (Carpan): 1,664,525 (Park & Miller'in onerisi)
- **c** (Artis): 1,013,904,223 (Numerical Recipes)
- **X0** (Seed): Baslangic degeri

## Ozellikler

- Sifirdan yazilmis LCG algoritmasi
- Coklu rastgele sayi fonksiyonlari (random, randint, choice, shuffle, sample)
- Istatistiksel analiz araclari (Dagilim analizi, Chi-Square testi)
- Gorsellestirmeler (Histogram, 2D/3D scatter plot)
- 8 farkli kullanim ornegi
- Detayli dokumantasyon

## Dosya Yapisi

```
RASTGELE SAYI/
│
├── random_generator.py    # Ana LCG algoritmasi
├── visualize.py          # Istatistiksel analiz ve gorsellestirme
├── examples.py           # 8 farkli kullanim ornegi
├── requirements.txt      # Gerekli kutuphaneler
├── README.md            # Bu dosya
└── .gitignore           # Git ignore dosyasi
```

## Kurulum

### 1. Gerekli Kutuphaneleri Yukleyin

```bash
pip install -r requirements.txt
```

### 2. Temel Kullanim

```python
from random_generator import LCGRandomGenerator

rng = LCGRandomGenerator(seed=42)

print(rng.random())

print(rng.randint(1, 100))

fruits = ["Elma", "Armut", "Muz"]
print(rng.choice(fruits))
```

## Calistirma

### Ana Algoritma Testi

```bash
python random_generator.py
```

### Istatistiksel Analiz ve Gorsellestirme

```bash
python visualize.py
```

Bu komut asagidaki dosyalari olusturur:
- `histogram.png` - Dagilim histogrami
- `scatter_2d.png` - 2D korelasyon grafigi
- `scatter_3d.png` - 3D korelasyon grafigi

### Kullanim Ornekleri

```bash
python examples.py
```

Bu komut 8 farkli ornek senaryoyu calistirir:
1. Temel kullanim
2. Zar atma simulasyonu
3. Piyango numarasi uretme
4. Rastgele sifre olusturma
5. Monte Carlo ile Pi tahmini
6. Kart destesi karistirma
7. Agirlikli rastgele secim
8. Rastgele yuruyus simulasyonu

## API Referansi

### `LCGRandomGenerator` Sinifi

#### `__init__(seed=None)`
Ureticiyi baslatir. Seed verilmezse sistem zamani kullanilir.

#### `random() -> float`
0.0 ile 1.0 arasinda rastgele ondalik sayi dondurur.

#### `randint(a, b) -> int`
a ile b arasinda (ikisi de dahil) rastgele tam sayi dondurur.

#### `choice(sequence) -> any`
Verilen listeden rastgele bir eleman secer.

#### `shuffle(items) -> list`
Listeyi Fisher-Yates algoritmasi ile karistirir.

#### `sample(population, k) -> list`
Populasyondan k adet benzersiz rastgele ornek secer.

#### `reset(seed=None)`
Ureticiyi yeniden baslatir.

#### `get_state() -> dict`
Uretecin mevcut durumunu dondurur.

## Istatistiksel Testler

Proje, uretilen sayilarin kalitesini degerlendirmek icin su testleri icerir:

1. **Dagilim Analizi**: Ortalama, standart sapma, min/max degerler
2. **Chi-Square Testi**: Uniform dagilim kontrolu
3. **Korelasyon Analizi**: 2D ve 3D scatter plot'lar ile gorsel inceleme

## Kullanim Senaryolari

- Oyun gelistirme (zar, kart oyunlari)
- Guvenli olmayan sifre/token uretimi
- Monte Carlo simulasyonlari
- Egitim ve ogretim amacli
- Piyango ve rastgele secim sistemleri

## Onemli Notlar

**Kriptografik Amaclar Icin Kullanmayin!**

LCG algoritmasi deterministiktir ve tahmin edilebilirdir. Guvenlik gerektiren uygulamalar icin (sifreleme, guvenli token uretimi vb.) `secrets` modulunu kullanin.

**Egitim Amacli**

Bu proje, rastgele sayi uretimi algoritmalarini ogretmek icin tasarlanmistir. Uretim ortaminda Python'un yerlesik `random` modulunu kullanmaniz onerilir.

## Referanslar

- [Wikipedia - Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator)
- Numerical Recipes in C (Press, Teukolsky, Vetterling, Flannery)
- Park, S. K., & Miller, K. W. (1988). Random Number Generators: Good Ones Are Hard To Find

## Yazar

**Suzan**  
Beyza Hoca - Kriptografi Dersi Projesi
