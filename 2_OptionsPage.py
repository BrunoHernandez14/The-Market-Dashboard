import streamlit as st
from streamlit_autorefresh import st_autorefresh
import yfinance as yf
import time
import datetime as datetime
import plotly.graph_objects as go
import pandas as pd


st.set_page_config(page_title="Options Dashboard")

# Name for DashBoard
st.title("Options Dashboard")

#Selecting a stock to view 
stock = st.sidebar.text_input("Enter a stock", "NVDA")
st.subheader(stock)

st.subheader("Meet the Greeks")

