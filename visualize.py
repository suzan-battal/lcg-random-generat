import matplotlib.pyplot as plt
import numpy as np
from random_generator import LCGRandomGenerator


def analyze_distribution(rng, sample_size=10000):
    print(f"\n{'='*60}")
    print("DAGILIM ANALIZI")
    print(f"{'='*60}")
    
    samples = [rng.random() for _ in range(sample_size)]
    
    mean = np.mean(samples)
    std = np.std(samples)
    min_val = np.min(samples)
    max_val = np.max(samples)
    
    print(f"\nOrnek Sayisi: {sample_size:,}")
    print(f"Ortalama: {mean:.6f} (Beklenen: 0.500000)")
    print(f"Standart Sapma: {std:.6f} (Beklenen: 0.288675)")
    print(f"Minimum: {min_val:.6f}")
    print(f"Maksimum: {max_val:.6f}")
    
    mean_error = abs(mean - 0.5) / 0.5 * 100
    std_error = abs(std - (1/np.sqrt(12))) / (1/np.sqrt(12)) * 100
    
    print(f"\nOrtalama Hata: %{mean_error:.2f}")
    print(f"Std Sapma Hata: %{std_error:.2f}")
    
    return samples


def plot_histogram(samples, bins=50):
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.7, color='#3498db', edgecolor='black')
    plt.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Ideal Uniform Dagilim')
    plt.title('LCG Rastgele Sayi Dagilimi (Histogram)', fontsize=16, fontweight='bold')
    plt.xlabel('Deger', fontsize=12)
    plt.ylabel('Yogunluk', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/Users/suzan/RASTGELE SAYI/histogram.png', dpi=300, bbox_inches='tight')
    print("\nHistogram kaydedildi: histogram.png")


def plot_2d_distribution(samples):
    x = samples[:-1]
    y = samples[1:]
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, alpha=0.3, s=1, color='#e74c3c')
    plt.title('2D Korelasyon Grafigi (Ardisik Sayi Ciftleri)', fontsize=16, fontweight='bold')
    plt.xlabel('X(n)', fontsize=12)
    plt.ylabel('X(n+1)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig('/Users/suzan/RASTGELE SAYI/scatter_2d.png', dpi=300, bbox_inches='tight')
    print("2D Scatter grafigi kaydedildi: scatter_2d.png")


def plot_3d_distribution(samples):
    x = samples[:-2]
    y = samples[1:-1]
    z = samples[2:]
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, alpha=0.2, s=1, color='#9b59b6')
    ax.set_title('3D Korelasyon Grafigi (Ardisik Sayi Ucluleri)', fontsize=16, fontweight='bold')
    ax.set_xlabel('X(n)', fontsize=10)
    ax.set_ylabel('X(n+1)', fontsize=10)
    ax.set_zlabel('X(n+2)', fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    plt.tight_layout()
    plt.savefig('/Users/suzan/RASTGELE SAYI/scatter_3d.png', dpi=300, bbox_inches='tight')
    print("3D Scatter grafigi kaydedildi: scatter_3d.png")


def chi_square_test(samples, bins=10):
    print(f"\n{'='*60}")
    print("CHI-SQUARE UNIFORMLUK TESTI")
    print(f"{'='*60}")
    
    observed, _ = np.histogram(samples, bins=bins, range=(0, 1))
    expected = len(samples) / bins
    
    chi_square = np.sum((observed - expected)**2 / expected)
    
    print(f"\nKutu Sayisi: {bins}")
    print(f"Beklenen Frekans: {expected:.2f}")
    print(f"Chi-Square Degeri: {chi_square:.4f}")
    
    df = bins - 1
    
    critical_values = {
        9: 16.919,
        19: 30.144,
        49: 66.339,
        99: 123.225
    }
    
    critical = critical_values.get(df, "Bilinmiyor")
    
    print(f"Serbestlik Derecesi: {df}")
    print(f"Kritik Deger (a=0.05): {critical}")
    
    if isinstance(critical, float):
        if chi_square < critical:
            print(f"\nTest BASARILI! Dagilim uniform olarak kabul edilebilir.")
        else:
            print(f"\nTest BASARISIZ! Dagilim uniform degil.")
    
    return chi_square


def run_full_analysis():
    print("\n" + "="*60)
    print("LCG RASTGELE SAYI URETECI - TAM ANALIZ")
    print("="*60)
    
    rng = LCGRandomGenerator(seed=12345)
    
    print(f"\nSeed: {rng.seed}")
    print(f"Modulus (m): {rng.MODULUS:,}")
    print(f"Carpan (a): {rng.MULTIPLIER:,}")
    print(f"Artis (c): {rng.INCREMENT:,}")
    
    samples = analyze_distribution(rng, sample_size=50000)
    
    chi_square_test(samples, bins=50)
    
    print(f"\n{'='*60}")
    print("GORSELLESTIRMELER OLUSTURULUYOR...")
    print(f"{'='*60}")
    
    plot_histogram(samples, bins=50)
    plot_2d_distribution(samples[:10000])
    plot_3d_distribution(samples[:5000])
    
    print(f"\n{'='*60}")
    print("ANALIZ TAMAMLANDI!")
    print(f"{'='*60}")
    print("\nOlusturulan dosyalar:")
    print("   - histogram.png")
    print("   - scatter_2d.png")
    print("   - scatter_3d.png")
    print("\n")


if __name__ == "__main__":
    run_full_analysis()
