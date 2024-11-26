import pandas as pd
import requests
import time
from IPython.display import display, clear_output

# Function to fetch cryptocurrency data from Binance API
def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()
    return data

# Function to display the data (modify for Binance API response)
def display_data(data):
    # Access data using appropriate keys from Binance API response
    df = pd.DataFrame(data)
    # Example: Assuming "symbol", "lastPrice", "priceChange" are keys
    df = df[['symbol', 'lastPrice', 'priceChange']]
    df.columns = ['Cryptocurrency', 'Last Price (USD)', 'Price Change (USD)']
    display(df.sort_values(by='Last Price', ascending=False))  # Sort by last price

# ... rest of the code remains the same (plot_price_trends, export_data, main loop)

# Main loop (modify coin_ids if needed)
if __name__ == "__main__":
    while True:
        data = fetch_crypto_data()
        clear_output(wait=True)
        display_data(data)
        time.sleep(60)  # Update every 60 seconds
