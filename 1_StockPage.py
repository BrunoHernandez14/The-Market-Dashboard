import streamlit as st
from streamlit_autorefresh import st_autorefresh
import yfinance as yf
import datetime as datetime
import plotly.graph_objects as go

#st_autorefresh(interval=2500,limit=None)
st.set_page_config(page_title="Stock Dashboard")
# Name for DashBoard
st.title("Stock Dashboard")
st.sidebar.title("Settings")
#Stock dashboard
#Selecting a stock to view 
stock = st.sidebar.text_input("Enter a stock", "NVDA")
st.subheader(stock)

#Selecting TimeFrame to be shown
timeFrame = st.sidebar.selectbox("Time Frame", ("5d","1mo","3mo","6mo","1y"))

#Download the stock data creating a dataframe
ticker = yf.Ticker(stock)
data = ticker.history(period=timeFrame)

priceColumn, volumeColumn, highColumn, lowColumn = st.columns(4)
priceColumn.metric("Current Price", f"{data['Close'].iloc[-1]:.2f}")
volumeColumn.metric("Volume", data['Volume'].iloc[-1])
highColumn.metric("High", f"{data['High'].max():.2f}")
lowColumn.metric("Low", f"{data['Low'].min():.2f}")

#Creating the Candle Stick Chart 
fig = go.Figure(data=[go.Candlestick(x=data.index,open=data["Open"],high=data["High"],low=data["Low"]
                                     ,close=data["Close"])])
fig.update_layout(title=stock, xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=False)
st.plotly_chart(fig)

st.subheader(f"{stock} Information")
dividendColumn, peColumn, epsColumn = st.columns(3)
dividendColumn.metric("Dividend", f"{ticker.info.get('dividendYield'):.3f}%")
peColumn.metric("P/E Ratio", f"{ticker.info['trailingPE']:.2f}")
epsColumn.metric("EPS", f"{ticker.info['EPS']:.2f}")

