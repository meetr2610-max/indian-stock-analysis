import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Indian Stock Analysis Dashboard")

stocks = [
    'ICICIBANK.NS',
    'RELIANCE.NS',
    'INFY.NS',
    'HDFCBANK.NS',
    'TCS.NS'
]

selected_stock = st.selectbox("Select a stock", stocks)

data = yf.download(selected_stock, start='2020-01-01')

st.subheader("Recent Stock Data")
st.write(data.tail())

st.subheader("Closing Price Chart")

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(data['Close'])
ax.set_title(f"{selected_stock} Closing Price")

st.pyplot(fig)

returns = data['Close'].pct_change()

st.subheader("Risk Metrics")
st.write("Mean Return:", returns.mean())
st.write("Volatility:", returns.std())