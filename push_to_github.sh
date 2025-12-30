#!/bin/bash

# LCG Rastgele Sayı Üreteci - GitHub Push Script
# Bu script, projeyi GitHub'a yüklemek için gerekli komutları içerir

echo "=================================================="
echo "🚀 GitHub'a Yükleme Script'i"
echo "=================================================="
echo ""

# Kullanıcıdan GitHub bilgilerini al
echo "GitHub kullanıcı adınızı girin:"
read USERNAME

echo ""
echo "Repository adını girin (örn: lcg-random-generator):"
read REPO_NAME

echo ""
echo "=================================================="
echo "📋 Özet:"
echo "=================================================="
echo "Kullanıcı: $USERNAME"
echo "Repository: $REPO_NAME"
echo "URL: https://github.com/$USERNAME/$REPO_NAME"
echo ""
echo "Devam etmek için Enter'a basın (İptal için Ctrl+C)"
read

# Remote ekle
echo ""
echo "🔗 Remote ekleniyor..."
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"

if [ $? -eq 0 ]; then
    echo "✅ Remote başarıyla eklendi!"
else
    echo "⚠️ Remote eklenemedi. Muhtemelen zaten eklenmiş."
    echo "   Eski remote kaldırılıyor ve yeniden ekleniyor..."
    git remote remove origin
    git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"
fi

# Push et
echo ""
echo "📤 GitHub'a push ediliyor..."
echo ""
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "✅ BAŞARILI!"
    echo "=================================================="
    echo ""
    echo "🎉 Projeniz GitHub'a yüklendi!"
    echo ""
    echo "📎 Repository Linki:"
    echo "   https://github.com/$USERNAME/$REPO_NAME"
    echo ""
    echo "🌐 Web'de görüntülemek için:"
    echo "   open https://github.com/$USERNAME/$REPO_NAME"
    echo ""
    echo "=================================================="
else
    echo ""
    echo "=================================================="
    echo "❌ HATA!"
    echo "=================================================="
    echo ""
    echo "Push işlemi başarısız oldu."
    echo ""
    echo "Olası nedenler:"
    echo "1. GitHub'da repository oluşturmadınız"
    echo "2. Yanlış kullanıcı adı veya repository adı"
    echo "3. Authentication hatası (token gerekli)"
    echo ""
    echo "Çözüm:"
    echo "1. https://github.com/new adresinden repository oluşturun"
    echo "2. Repository adının doğru olduğundan emin olun"
    echo "3. GitHub Personal Access Token kullanın (şifre yerine)"
    echo ""
fi
