import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App 

showing stock **closing price** and ***volume*** of Google!

""")

# Ticker Symbol:
tickerSymbol = 'GOOGL'

#Get Data for this ticker
tickerData = yf.Ticker(tickerSymbol)

#get historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-1-31', end='2021-1-31')


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)