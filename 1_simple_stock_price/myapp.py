import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of GOOGLE!

""")

#Ticker symbol is the unique series of letters assigned to a companies stocks for trading purposes.
tickerSymbol = 'GOOGL'

#Extract/Get data of the particular ticker symbol.
tickerData = yf.Ticker(tickerSymbol)


tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

#Volume and Stock Split
