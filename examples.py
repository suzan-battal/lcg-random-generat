from random_generator import LCGRandomGenerator


def example_1_basic_usage():
    print("\n" + "="*60)
    print("ORNEK 1: Temel Kullanim")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=42)
    
    print("\n5 rastgele sayi (0-1 arasi):")
    for i in range(5):
        print(f"  {i+1}. {rng.random():.6f}")


def example_2_dice_roll():
    print("\n" + "="*60)
    print("ORNEK 2: Zar Atma Simulasyonu")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    print("\n10 zar atisi:")
    for i in range(10):
        dice = rng.randint(1, 6)
        print(f"  Atis {i+1}: {dice}")
    
    print("\n1000 atislik zar istatistigi:")
    results = [rng.randint(1, 6) for _ in range(1000)]
    
    for num in range(1, 7):
        count = results.count(num)
        percentage = (count / 1000) * 100
        bar = '=' * int(percentage / 2)
        print(f"  {num}: {bar} {count} (%{percentage:.1f})")


def example_3_lottery():
    print("\n" + "="*60)
    print("ORNEK 3: Piyango Numarasi Uretme")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    print("\n5 farkli piyango kuponu (1-49 arasi 6 sayi):")
    for i in range(5):
        numbers = rng.sample(list(range(1, 50)), 6)
        numbers.sort()
        print(f"  Kupon {i+1}: {numbers}")


def example_4_password_generator():
    print("\n" + "="*60)
    print("ORNEK 4: Rastgele Sifre Olusturma")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    all_chars = list(lowercase + uppercase + digits + special)
    
    print("\n5 rastgele sifre (12 karakter):")
    for i in range(5):
        password = ''.join([rng.choice(all_chars) for _ in range(12)])
        print(f"  Sifre {i+1}: {password}")


def example_5_monte_carlo_pi():
    print("\n" + "="*60)
    print("ORNEK 5: Monte Carlo ile Pi Tahmini")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=42)
    
    samples = [10000, 100000, 1000000]
    
    print("\nFarkli ornek sayilari ile Pi tahmini:")
    for n in samples:
        inside_circle = 0
        
        for _ in range(n):
            x = rng.random()
            y = rng.random()
            
            if x*x + y*y <= 1:
                inside_circle += 1
        
        pi_estimate = 4 * inside_circle / n
        error = abs(pi_estimate - 3.14159265359) / 3.14159265359 * 100
        
        print(f"  {n:,} ornek: pi = {pi_estimate:.6f} (Hata: %{error:.3f})")


def example_6_card_shuffle():
    print("\n" + "="*60)
    print("ORNEK 6: Kart Destesi Karistirma")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    suits = ['S', 'H', 'D', 'C']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    
    print(f"\nOrijinal deste ({len(deck)} kart):")
    print("  " + " ".join(deck[:13]))
    
    shuffled = rng.shuffle(deck)
    
    print(f"\nKaristirilmis deste:")
    print("  " + " ".join(shuffled[:13]))
    
    print(f"\nOyunculara dagitilan kartlar:")
    for player in range(1, 5):
        hand = shuffled[(player-1)*5:player*5]
        print(f"  Oyuncu {player}: {' '.join(hand)}")


def example_7_weighted_random():
    print("\n" + "="*60)
    print("ORNEK 7: Agirlikli Rastgele Secim")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    items = ['Yaygin Esya'] * 70 + ['Nadir Esya'] * 25 + ['Efsanevi Esya'] * 5
    
    print("\n100 sandik acilisi simulasyonu:")
    
    results = {'Yaygin Esya': 0, 'Nadir Esya': 0, 'Efsanevi Esya': 0}
    
    for _ in range(100):
        item = rng.choice(items)
        results[item] += 1
    
    for item, count in results.items():
        bar = '=' * (count // 2)
        print(f"  {item:20s}: {bar} {count}")


def example_8_simulation():
    print("\n" + "="*60)
    print("ORNEK 8: Rastgele Yuruyus Simulasyonu (1D)")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=123)
    
    position = 0
    path = [position]
    
    print("\n20 adimlik rastgele yuruyus:")
    
    for step in range(20):
        if rng.random() < 0.5:
            position -= 1
            direction = "Sol"
        else:
            position += 1
            direction = "Sag"
        
        path.append(position)
        print(f"  Adim {step+1:2d}: {direction} Pozisyon: {position:+3d}")
    
    print(f"\nBaslangic: 0")
    print(f"Bitis: {position:+d}")
    print(f"Net Yer Degistirme: {abs(position)} birim")


def run_all_examples():
    print("\n" + "="*70)
    print("LCG RASTGELE SAYI URETECI - KULLANIM ORNEKLERI")
    print("="*70)
    
    example_1_basic_usage()
    example_2_dice_roll()
    example_3_lottery()
    example_4_password_generator()
    example_5_monte_carlo_pi()
    example_6_card_shuffle()
    example_7_weighted_random()
    example_8_simulation()
    
    print("\n" + "="*70)
    print("TUM ORNEKLER TAMAMLANDI!")
    print("="*70)
    print("\n")


if __name__ == "__main__":
    run_all_examples()
