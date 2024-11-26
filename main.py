# Import necessary libraries
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import requests
import plotly.graph_objs as go

# Function to fetch cryptocurrency data from Binance API
def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

# Fetch initial data
df = fetch_crypto_data()

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Cryptocurrency Overview"),
    dcc.Dropdown(
        id='crypto-dropdown',
        options=[{'label': symbol, 'value': symbol} for symbol in df['symbol']],
        value='BTCUSDT',  # Default value
        clearable=False,
    ),
    dcc.Graph(id='price-chart'),
    html.Button("Download CSV", id='download-button'),
    dcc.Download(id="download-dataframe-csv"),
])

# Callback to update the graph based on selected cryptocurrency
@app.callback(
    Output('price-chart', 'figure'),
    Input('crypto-dropdown', 'value')
)
def update_graph(selected_crypto):
    # Filter DataFrame for selected cryptocurrency
    col_df = df[df['symbol'] == selected_crypto]
    
    # Create a line chart for price change over time (mock data for demonstration)
    figure = go.Figure()
    
    # Use mock historical data for demonstration purposes (replace with actual historical data if available)
    historical_prices = [float(col_df['weightedAvgPrice'].values[0])] * 10  # Mocking same price for simplicity
    figure.add_trace(go.Scatter(
        x=list(range(10)),  # Mock time series
        y=historical_prices,
        mode='lines+markers',
        name=selected_crypto,
        line=dict(shape='linear')
    ))
    
    figure.update_layout(title=f'{selected_crypto} Price Over Time',
                          xaxis_title='Time',
                          yaxis_title='Price (USDT)')
    
    return figure

# Callback to download CSV data
@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("download-button", "n_clicks"),
)
def download_csv(n_clicks):
    if n_clicks:
        return dcc.send_data_frame(df.to_csv, "cryptocurrency_data.csv", index=False)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
