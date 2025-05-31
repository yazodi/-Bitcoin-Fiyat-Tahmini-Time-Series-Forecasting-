import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Sayfa ayarları
st.set_page_config(page_title="Bitcoin Fiyat Tahmini", layout="centered")
st.title("📈 Bitcoin Fiyat Tahmini - LSTM")

# Model ve veri yükleme
@st.cache_resource
def load_trained_model():
    return load_model("btc_lstm_model.keras")

@st.cache_data
def load_data():
    df = pd.read_csv("BTC_USD_Sample_2020_2024.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

model = load_trained_model()
df = load_data()

# Veriyi hazırlama
scaler = MinMaxScaler()
data = df['Close'].values.reshape(-1, 1)
scaled_data = scaler.fit_transform(data)

# Tahmin fonksiyonu
@st.cache_data
def predict_future_days(days=30):
    last_60_days = scaled_data[-60:]
    future_predictions = []
    input_seq = last_60_days

    for _ in range(days):
        pred_input = input_seq[-60:].reshape(1, 60, 1)
        pred = model.predict(pred_input)[0][0]
        future_predictions.append(pred)
        input_seq = np.append(input_seq, [[pred]], axis=0)

    return scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# Gün seçimi
future_days = st.slider("Kaç günlük fiyat tahmini istiyorsunuz?", 1, 60, 30)

if st.button("Tahmini Başlat"):
    preds = predict_future_days(future_days)
    future_dates = pd.date_range(df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=future_days)

    st.subheader("📊 Tahmini Fiyatlar")
    forecast_df = pd.DataFrame({"Tarih": future_dates, "Tahmini Fiyat (USD)": preds.flatten()})
    st.dataframe(forecast_df)

    # Grafik
    plt.figure(figsize=(10,4))
    plt.plot(future_dates, preds, label='Tahmini Fiyat')
    plt.title("Bitcoin Gelecek Tahmini")
    plt.xlabel("Tarih")
    plt.ylabel("USD")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
