"""
Kullanım Örnekleri
==================

Bu dosya, LCG rastgele sayı üretecinin çeşitli kullanım senaryolarını gösterir.
"""

from random_generator import LCGRandomGenerator


def example_1_basic_usage():
    """Örnek 1: Temel kullanım"""
    print("\n" + "="*60)
    print("📚 ÖRNEK 1: Temel Kullanım")
    print("="*60)
    
    # Üreteci oluştur
    rng = LCGRandomGenerator(seed=42)
    
    # Rastgele sayılar üret
    print("\n5 rastgele sayı (0-1 arası):")
    for i in range(5):
        print(f"  {i+1}. {rng.random():.6f}")


def example_2_dice_roll():
    """Örnek 2: Zar atma simülasyonu"""
    print("\n" + "="*60)
    print("🎲 ÖRNEK 2: Zar Atma Simülasyonu")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    print("\n10 zar atışı:")
    for i in range(10):
        dice = rng.randint(1, 6)
        print(f"  Atış {i+1}: {'🎲' * dice} = {dice}")
    
    # İstatistik
    print("\n1000 atışlık zar istatistiği:")
    results = [rng.randint(1, 6) for _ in range(1000)]
    
    for num in range(1, 7):
        count = results.count(num)
        percentage = (count / 1000) * 100
        bar = '█' * int(percentage / 2)
        print(f"  {num}: {bar} {count} (%{percentage:.1f})")


def example_3_lottery():
    """Örnek 3: Piyango numarası üretme"""
    print("\n" + "="*60)
    print("🎰 ÖRNEK 3: Piyango Numarası Üretme")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    print("\n5 farklı piyango kuponu (1-49 arası 6 sayı):")
    for i in range(5):
        numbers = rng.sample(list(range(1, 50)), 6)
        numbers.sort()
        print(f"  Kupon {i+1}: {numbers}")


def example_4_password_generator():
    """Örnek 4: Rastgele şifre oluşturma"""
    print("\n" + "="*60)
    print("🔐 ÖRNEK 4: Rastgele Şifre Oluşturma")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    # Karakter setleri
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    all_chars = list(lowercase + uppercase + digits + special)
    
    print("\n5 rastgele şifre (12 karakter):")
    for i in range(5):
        password = ''.join([rng.choice(all_chars) for _ in range(12)])
        print(f"  Şifre {i+1}: {password}")


def example_5_monte_carlo_pi():
    """Örnek 5: Monte Carlo ile Pi tahmini"""
    print("\n" + "="*60)
    print("🥧 ÖRNEK 5: Monte Carlo ile Pi Tahmini")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=42)
    
    samples = [10000, 100000, 1000000]
    
    print("\nFarklı örnek sayıları ile Pi tahmini:")
    for n in samples:
        inside_circle = 0
        
        for _ in range(n):
            x = rng.random()
            y = rng.random()
            
            # Birim karenin içinde birim çembere düşen noktalar
            if x*x + y*y <= 1:
                inside_circle += 1
        
        pi_estimate = 4 * inside_circle / n
        error = abs(pi_estimate - 3.14159265359) / 3.14159265359 * 100
        
        print(f"  {n:,} örnek: π ≈ {pi_estimate:.6f} (Hata: %{error:.3f})")


def example_6_card_shuffle():
    """Örnek 6: Kart destesi karıştırma"""
    print("\n" + "="*60)
    print("🃏 ÖRNEK 6: Kart Destesi Karıştırma")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    # Kart destesi
    suits = ['♠️', '♥️', '♦️', '♣️']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    
    print(f"\nOrijinal deste ({len(deck)} kart):")
    print("  " + " ".join(deck[:13]))  # İlk 13 kartı göster
    
    # Karıştır
    shuffled = rng.shuffle(deck)
    
    print(f"\nKarıştırılmış deste:")
    print("  " + " ".join(shuffled[:13]))  # İlk 13 kartı göster
    
    # 5 kart dağıt
    print(f"\nOyunculara dağıtılan kartlar:")
    for player in range(1, 5):
        hand = shuffled[(player-1)*5:player*5]
        print(f"  Oyuncu {player}: {' '.join(hand)}")


def example_7_weighted_random():
    """Örnek 7: Ağırlıklı rastgele seçim"""
    print("\n" + "="*60)
    print("⚖️ ÖRNEK 7: Ağırlıklı Rastgele Seçim")
    print("="*60)
    
    rng = LCGRandomGenerator()
    
    # Ödül havuzu (yaygın, nadir, efsanevi)
    items = ['Yaygın Eşya'] * 70 + ['Nadir Eşya'] * 25 + ['Efsanevi Eşya'] * 5
    
    print("\n100 sandık açılışı simülasyonu:")
    
    results = {'Yaygın Eşya': 0, 'Nadir Eşya': 0, 'Efsanevi Eşya': 0}
    
    for _ in range(100):
        item = rng.choice(items)
        results[item] += 1
    
    for item, count in results.items():
        bar = '█' * (count // 2)
        print(f"  {item:20s}: {bar} {count}")


def example_8_simulation():
    """Örnek 8: Basit rastgele yürüyüş simülasyonu"""
    print("\n" + "="*60)
    print("🚶 ÖRNEK 8: Rastgele Yürüyüş Simülasyonu (1D)")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=123)
    
    position = 0
    path = [position]
    
    print("\n20 adımlık rastgele yürüyüş:")
    
    for step in range(20):
        # %50 sağa, %50 sola
        if rng.random() < 0.5:
            position -= 1
            direction = "←"
        else:
            position += 1
            direction = "→"
        
        path.append(position)
        print(f"  Adım {step+1:2d}: {direction} Pozisyon: {position:+3d}")
    
    print(f"\n📍 Başlangıç: 0")
    print(f"📍 Bitiş: {position:+d}")
    print(f"📍 Net Yer Değiştirme: {abs(position)} birim")


def run_all_examples():
    """Tüm örnekleri çalıştırır"""
    print("\n" + "="*70)
    print("🎯 LCG RASTGELE SAYI ÜRETECİ - KULLANIM ÖRNEKLERİ")
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
    print("✅ TÜM ÖRNEKLER TAMAMLANDI!")
    print("="*70)
    print("\n")


if __name__ == "__main__":
    run_all_examples()
