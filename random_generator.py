"""
Linear Congruential Generator (LCG) - Rastgele Sayı Üreteci
============================================================

Bu modül, matematiksel olarak kanıtlanmış Linear Congruential Generator (LCG)
algoritmasını kullanarak rastgele sayılar üretir.

LCG Formülü: X(n+1) = (a * X(n) + c) mod m

Parametreler:
- m: Modulus (2^32 = 4294967296) - Maksimum değer
- a: Çarpan (1664525) - Park ve Miller'in önerdiği değer
- c: Artış (1013904223) - Numerical Recipes'tan
- seed: Başlangıç değeri

Yazar: [İsminiz]
Tarih: 30 Aralık 2025
"""

import time


class LCGRandomGenerator:
    """Linear Congruential Generator rastgele sayı üreteci sınıfı"""
    
    # LCG parametreleri (Numerical Recipes'tan alınmıştır)
    MODULUS = 2**32  # m = 4294967296
    MULTIPLIER = 1664525  # a (Park & Miller)
    INCREMENT = 1013904223  # c
    
    def __init__(self, seed=None):
        """
        LCG üretecini başlatır
        
        Args:
            seed (int, optional): Başlangıç değeri. None ise sistem zamanı kullanılır.
        """
        if seed is None:
            # Seed verilmediyse sistem zamanını kullan
            seed = int(time.time() * 1000) % self.MODULUS
        
        self.seed = seed
        self.current = seed
    
    def next(self):
        """
        Bir sonraki rastgele sayıyı üretir
        
        Returns:
            int: 0 ile MODULUS-1 arasında bir tam sayı
        """
        self.current = (self.MULTIPLIER * self.current + self.INCREMENT) % self.MODULUS
        return self.current
    
    def random(self):
        """
        0 ile 1 arasında rastgele ondalık sayı üretir
        
        Returns:
            float: 0.0 ile 1.0 arasında bir sayı
        """
        return self.next() / self.MODULUS
    
    def randint(self, a, b):
        """
        a ile b arasında (ikisi de dahil) rastgele tam sayı üretir
        
        Args:
            a (int): Alt sınır
            b (int): Üst sınır
        
        Returns:
            int: a ile b arasında bir tam sayı
        """
        return a + int(self.random() * (b - a + 1))
    
    def choice(self, sequence):
        """
        Verilen listeden rastgele bir eleman seçer
        
        Args:
            sequence (list): Seçim yapılacak liste
        
        Returns:
            Listeden rastgele seçilen bir eleman
        """
        if not sequence:
            raise ValueError("Boş bir listeden seçim yapılamaz")
        
        index = self.randint(0, len(sequence) - 1)
        return sequence[index]
    
    def shuffle(self, items):
        """
        Verilen listeyi rastgele karıştırır (Fisher-Yates algoritması)
        
        Args:
            items (list): Karıştırılacak liste
        
        Returns:
            list: Karıştırılmış liste
        """
        result = items.copy()
        n = len(result)
        
        for i in range(n - 1, 0, -1):
            j = self.randint(0, i)
            result[i], result[j] = result[j], result[i]
        
        return result
    
    def sample(self, population, k):
        """
        Popülasyondan k adet benzersiz rastgele örnek seçer
        
        Args:
            population (list): Ana liste
            k (int): Seçilecek eleman sayısı
        
        Returns:
            list: Rastgele seçilen k eleman
        """
        if k > len(population):
            raise ValueError("Örnek sayısı popülasyondan büyük olamaz")
        
        shuffled = self.shuffle(population)
        return shuffled[:k]
    
    def reset(self, seed=None):
        """
        Üreteciyi yeniden başlatır
        
        Args:
            seed (int, optional): Yeni başlangıç değeri
        """
        if seed is None:
            seed = self.seed
        
        self.current = seed
    
    def get_state(self):
        """
        Üretecin mevcut durumunu döndürür
        
        Returns:
            dict: Mevcut durum bilgileri
        """
        return {
            'seed': self.seed,
            'current': self.current,
            'modulus': self.MODULUS,
            'multiplier': self.MULTIPLIER,
            'increment': self.INCREMENT
        }


# Test kodu
if __name__ == "__main__":
    print("=" * 60)
    print("LCG Rastgele Sayı Üreteci - Test")
    print("=" * 60)
    
    # Üreteci başlat
    rng = LCGRandomGenerator(seed=42)
    
    print(f"\n📊 Başlangıç Seed: {rng.seed}")
    print(f"📊 Parametreler: m={rng.MODULUS}, a={rng.MULTIPLIER}, c={rng.INCREMENT}")
    
    # Test 1: 0-1 arası ondalık sayılar
    print("\n🔢 Test 1: 10 adet 0-1 arası rastgele sayı:")
    random_floats = [rng.random() for _ in range(10)]
    for i, val in enumerate(random_floats, 1):
        print(f"  {i:2d}. {val:.6f}")
    
    # Test 2: Belirli aralıkta tam sayılar
    print("\n🎲 Test 2: 1-100 arası 15 rastgele tam sayı:")
    random_ints = [rng.randint(1, 100) for _ in range(15)]
    print(f"  {random_ints}")
    
    # Test 3: Liste karıştırma
    print("\n🔀 Test 3: Liste karıştırma:")
    original = list(range(1, 11))
    shuffled = rng.shuffle(original)
    print(f"  Orijinal: {original}")
    print(f"  Karışık:  {shuffled}")
    
    # Test 4: Rastgele seçim
    print("\n🎯 Test 4: 5 rastgele meyve seçimi:")
    fruits = ["🍎 Elma", "🍊 Portakal", "🍌 Muz", "🍇 Üzüm", "🍓 Çilek"]
    for i in range(5):
        print(f"  Seçim {i+1}: {rng.choice(fruits)}")
    
    # Test 5: Durum bilgisi
    print("\n⚙️ Test 5: Üretici durumu:")
    state = rng.get_state()
    for key, value in state.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("✅ Tüm testler tamamlandı!")
    print("=" * 60)
