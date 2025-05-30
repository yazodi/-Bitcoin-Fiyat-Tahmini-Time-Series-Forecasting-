
BTC_USD_Sample_2020_2024 hazır veri kullanıldı

Grafikte gördüğün gibi:

Mavi çizgi → Gerçek BTC fiyatları (2020–2024 arası)

Turuncu çizgi → Modelin gelecek 30 gün için yaptığı tahmin

Model geçmişi güzel öğrenmiş ve kısa vadeli tahminlerde istikrarlı bir gidişat yakalamış.

📦 Bitcoin Fiyat Tahmini — Özet (README için kısa notlar)
Proje Amacı:
Geçmiş BTC-USD verilerini kullanarak, LSTM modeliyle 30 günlük fiyat tahmini yapmak.

Adımlar:

Veriyi yfinance veya CSV ile aldık.

Kapanış fiyatlarını görselleştirdik.

MinMaxScaler ile veriyi ölçekledik.

60 günlük dilimler oluşturup LSTM modeliyle eğittik.

Modelin eğitimi sonucunda gerçek ve tahmin fiyatlarını karşılaştırdık.

Son olarak gelecekteki 30 gün için fiyat tahmin ettik.