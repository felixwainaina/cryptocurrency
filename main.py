import streamlit as st
import pandas as pd
from pygments.lexers import go

st.set_page_config(page_icon="🗠", page_title="Cryptocurrency Overview", layout="centered", initial_sidebar_state="auto")

st.sidebar.image(
    "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/z3ahdkytzwi1jxlpazje",
    width=50,
)

c1, c2 = st.columns([1, 8])

with c1:
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/chart-increasing_1f4c8.png",
        width=90,
    )

st.markdown(
    """# **Crypto Overview**
Cryptocurrency price app
"""
)

st.header("**Selected Crypto Price**")

# Load market data from Binance API
df = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")


# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a



crpytoList = {
    "Price 1": "BTCBUSD",
    "Price 2": "ETHBUSD",
    "Price 3": "BNBBUSD",
    "Price 4": "XRPBUSD",
    "Price 5": "ADABUSD",
    "Price 6": "DOGEBUSD",
    "Price 7": "SHIBBUSD",
    "Price 8": "DOTBUSD",
    "Price 9": "MATICBUSD",
    "Price 10": "MATICBUSD",
    "Price 11": "MATICBUSD",
    "Price 12": "MATICBUSD",
}


col1, col2, col3, col4  = st.columns(4)


for i in range(len(crpytoList.keys())):
    selected_crypto_label = list(crpytoList.keys())[i]
    selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
    selected_crypto = st.sidebar.selectbox(
        selected_crypto_label, df.symbol, selected_crypto_index, key=str(i)
    )
    col_df = df[df.symbol == selected_crypto]
    col_price = round_value(col_df.weightedAvgPrice)
    col_percent = f"{float(col_df.priceChangePercent)}%"
    if i < 3:
        with col1:
            st.metric(selected_crypto, col_price, col_percent)
    if 2 < i < 6:
        with col2:
            st.metric(selected_crypto, col_price, col_percent)
    if i > 5:
        with col3:
            st.metric(selected_crypto, col_price, col_percent)

st.header("")


col_df.line_chart()
# st.download_button(
#    label="Download data as CSV",
#    data=df,
#    #file_name='large_df.csv',
#    # mime='text/csv'
#    )


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)

st.dataframe(df, height=2000)

