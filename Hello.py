import streamlit as st

st.set_page_config(page_title="Hello!")

st.title("Welcome to my Stock and Options Dashboard")
st.header("What is it about?")
st.write("This is an application I created in order to calculate and display stock data, "
"and evaluate the greek values as well as the involuntary volatility for options contracts! " \
" As I continue programming this I plan on adding technical indicators(RSI,SMA,EMA) as well as some algorithmic trading formulas!" \
" All the greek values and IV will be calculated from the data I have gathered in order to teach myself how to utilize" \
"them since they are routinely used in quantative finance!")

