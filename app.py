import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Indian Stock Analysis Dashboard")

start_date = st.date_input("Start Date", value=None)
end_date = st.date_input("End Date", value=None)

stocks = [
    'ICICIBANK.NS',
    'RELIANCE.NS',
    'INFY.NS',
    'HDFCBANK.NS',
    'TCS.NS'
]

selected_stock = st.selectbox("Select a stock", stocks)

analyze = st.button("Analyze Stock", use_container_width=True)

if analyze:
    with st.spinner("Fetching stock data..."):
        data = yf.download(selected_stock, start=start_date, end=end_date)

    if data.empty:
        st.error("No stock data found.")
        st.stop()

    st.subheader("Recent Stock Data")
    st.write(data.tail())

    data['MA50'] = data['Close'].rolling(50).mean()
    data['MA200'] = data['Close'].rolling(200).mean()

    st.subheader("Closing Price Chart")

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(data['Close'], label='Closing Price')
    ax.plot(data['MA50'], label='50-Day MA')
    ax.plot(data['MA200'], label='200-Day MA')

    ax.legend()
    st.pyplot(fig)

    # THIS must come before mean/std
    returns = data['Close'].squeeze().pct_change().dropna()

    mean_return = returns.mean().item()
    volatility = returns.std().item()

    st.subheader("Risk Metrics")
    st.write("Mean Return:", f"{mean_return*100:.2f}%")
    st.write("Volatility:", f"{volatility*100:.2f}%")