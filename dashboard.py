#CREATING A FINANCE DASHBOARD TO COMPARE THE MOVEMENT OF TRADABLE SECURITIES

import streamlit as st
import yfinance as yf
import pandas as pd

#Let's make a heading for the dashboard
st.title('Finance Dashboard: Monitor Tradable Securities')

#The line below allow add assets that we would want to compare
tickers = ('TSLA', 'AAPL', 'MSFT','BTC-USD', 'ETH-USD', 'EURUSD=X')

#Let's create a dropdown menu that we would want to add assets from
dropdown = st.multiselect('Pick your assets', tickers)

#Define our dates  (Start and End dates)
start = st.date_input('Start Data', value= pd.to_datetime('2021-01-01'))
end = st.date_input('End Date', value=pd.to_datetime('today'))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    return cumret

#let's get live asset data and  plot the assets
if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Return of {}'.format(dropdown))
    #plot the line
    st.line_chart(df)

