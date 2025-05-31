

---
tags:
- time-series
- bitcoin
- lstm
- forecasting
- keras
- deep-learning
---


# 📈 Bitcoin LSTM Fiyat Tahmini Modeli

Bu model, 2020–2024 tarihleri arasında Bitcoin kapanış fiyatlarına bakarak LSTM kullanarak zaman serisi tahmini yapmaktadır.

Kullanım Alanları
Kripto fiyat tahmini



## 🧠 Model Özellikleri

- Model tipi: LSTM
- Girdi: Son 60 günün kapanış fiyatı
- Çıktı: Bir sonraki günün tahmini fiyatı
- Eğitim veri kümesi: BTC_USD_Sample_2020_2024.csv



## 🔧 Kullanılan Araçlar
- Python
- TensorFlow / Keras
- Streamlit
- LSTM Modeli (60 günlük pencere ile tahmin)

## 📁 Dosyalar
- `btc_lstm_model.keras`: Eğitilmiş model dosyası
- `BTC_USD_Sample_2020_2024.csv`: Veri seti
- `app.py`: Streamlit uygulaması

## 🔗 Hugging Face
Model dosyasına şu bağlantıdan ulaşabilirsiniz:
👉 [https://huggingface.co/yazodi/Bitcoin_Fiyat_Tahmini_Time_Series_Forecasting](https://huggingface.co/yazodi/Bitcoin_Fiyat_Tahmini_Time_Series_Forecasting)

## 🖼️ Ekran Görüntüsü
![Tahmin Ekranı](Screenshot_3.png)

## 🚀 Başlatmak için
```bash
streamlit run app.py
```

## 📦 Gerekli Paketler (`requirements.txt`)
```txt
streamlit
numpy
pandas
matplotlib
scikit-learn
tensorflow
``` 
    """)

📝 Lisans
MIT License