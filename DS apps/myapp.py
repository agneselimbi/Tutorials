import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    # Simple Stock Price App

    Shows the stock closing price and volume of Google!
    """)
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get historical data of Google stock price
tickerData = yf.Ticker(tickerSymbol)
# create a DataFrame
tickerDf = tickerData.history(period ='id', start ='2010-5-31', end ='2021-5-31')
st.write("""## Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""## Volume Price""")
st.line_chart(tickerDf.Volume)
