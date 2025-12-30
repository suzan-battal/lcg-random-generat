import time


class LCGRandomGenerator:
    
    MODULUS = 2**32
    MULTIPLIER = 1664525
    INCREMENT = 1013904223
    
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000) % self.MODULUS
        
        self.seed = seed
        self.current = seed
    
    def next(self):
        self.current = (self.MULTIPLIER * self.current + self.INCREMENT) % self.MODULUS
        return self.current
    
    def random(self):
        return self.next() / self.MODULUS
    
    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))
    
    def choice(self, sequence):
        if not sequence:
            raise ValueError("Bos bir listeden secim yapilamaz")
        
        index = self.randint(0, len(sequence) - 1)
        return sequence[index]
    
    def shuffle(self, items):
        result = items.copy()
        n = len(result)
        
        for i in range(n - 1, 0, -1):
            j = self.randint(0, i)
            result[i], result[j] = result[j], result[i]
        
        return result
    
    def sample(self, population, k):
        if k > len(population):
            raise ValueError("Ornek sayisi populasyondan buyuk olamaz")
        
        shuffled = self.shuffle(population)
        return shuffled[:k]
    
    def reset(self, seed=None):
        if seed is None:
            seed = self.seed
        
        self.current = seed
    
    def get_state(self):
        return {
            'seed': self.seed,
            'current': self.current,
            'modulus': self.MODULUS,
            'multiplier': self.MULTIPLIER,
            'increment': self.INCREMENT
        }


if __name__ == "__main__":
    print("=" * 60)
    print("LCG Rastgele Sayi Ureteci - Test")
    print("=" * 60)
    
    rng = LCGRandomGenerator(seed=42)
    
    print(f"\nBaslangic Seed: {rng.seed}")
    print(f"Parametreler: m={rng.MODULUS}, a={rng.MULTIPLIER}, c={rng.INCREMENT}")
    
    print("\nTest 1: 10 adet 0-1 arasi rastgele sayi:")
    random_floats = [rng.random() for _ in range(10)]
    for i, val in enumerate(random_floats, 1):
        print(f"  {i:2d}. {val:.6f}")
    
    print("\nTest 2: 1-100 arasi 15 rastgele tam sayi:")
    random_ints = [rng.randint(1, 100) for _ in range(15)]
    print(f"  {random_ints}")
    
    print("\nTest 3: Liste karistirma:")
    original = list(range(1, 11))
    shuffled = rng.shuffle(original)
    print(f"  Orijinal: {original}")
    print(f"  Karisik:  {shuffled}")
    
    print("\nTest 4: 5 rastgele meyve secimi:")
    fruits = ["Elma", "Portakal", "Muz", "Uzum", "Cilek"]
    for i in range(5):
        print(f"  Secim {i+1}: {rng.choice(fruits)}")
    
    print("\nTest 5: Uretici durumu:")
    state = rng.get_state()
    for key, value in state.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("Tum testler tamamlandi!")
    print("=" * 60)
