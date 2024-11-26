import streamlit as st
import pandas as pd
import requests
# import plotly.graph_objs as go

# Function to fetch cryptocurrency data from Binance API
def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

# Fetch initial data
df = fetch_crypto_data()

# Streamlit app layout
st.set_page_config(page_title="Cryptocurrency Overview", page_icon="💰", layout="centered")
st.title("Cryptocurrency Overview")

# Dropdown for selecting cryptocurrency
selected_crypto = st.selectbox("Select Cryptocurrency:", df['symbol'].tolist(), index=0)

# Display selected cryptocurrency details
col_df = df[df['symbol'] == selected_crypto]
price = float(col_df['weightedAvgPrice'].values[0])
percent_change = f"{float(col_df['priceChangePercent'].values[0])}%"

st.metric(label=selected_crypto, value=f"${price:.2f}", delta=percent_change)

# Create a line chart for price change over time (mock data for demonstration)
historical_prices = [price] * 10  # Mocking same price for simplicity
time_series = list(range(10))  # Mock time series

# Create a Plotly figure
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=time_series,
    y=historical_prices,
    mode='lines+markers',
    name=selected_crypto,
    line=dict(shape='linear')
))

fig.update_layout(title=f'{selected_crypto} Price Over Time',
                  xaxis_title='Time',
                  yaxis_title='Price (USDT)')

# Display the line chart
st.plotly_chart(fig)

# Download button for CSV data
if st.button("Download Data as CSV"):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='cryptocurrency_data.csv',
        mime='text/csv'
    )

# Display full DataFrame
st.subheader("Full Cryptocurrency Data")
st.dataframe(df)
