import yfinance as yf
import streamlit as st

import pandas as pd

from gnewsclient import gnewsclient 
  
# declare a NewsClient object  
client = gnewsclient.NewsClient(language='Eng', location='india', topic='Business', max_results=5) 
news_list=client.get_news()
st.sidebar.write('# News related to business')
for item in news_list: 
    st.sidebar.write(" ### Title : ", item['title']) 
    
    st.sidebar.write(" ### Link : ", item['link'])
  






st.write("""
# Financial Stock Analysis App
## The app provides info abut the stocks of companies about the stock value,history and performance for last 30 years 
""")
name = st.text_input("Enter the symbol to know about particular Company",) 
st.write("Like for Google enter 'GOOGL'")
  
if(st.button('Submit')):
    st.write(name) 
    result = name.title() 
    a=yf.Ticker(name)
    b=['longBusinessSummary','marketCap','regularMarketOpen',"fiftyDayAverage",'averageVolume',"profitMargins"]
    c={'Business Summary':a.info['longBusinessSummary'],'Market Capital':a.info['marketCap'],'Regular market open':a.info['regularMarketOpen'],'Fifty day avg':a.info['fiftyDayAverage'],
'Average Volumne':a.info['averageVolume'],'Profit Margin':a.info['profitMargins']}
    st.write(c)

    st.write('### Historical Dataet of the comapny for last 30 years')
    aapl_historical =a.history(period='30y')
    st.write(aapl_historical)
    st.line_chart(aapl_historical['Volume'])
    st.write('')





    st.write('### Recommendations for buying or selling a company’s stock is provided by different Finacial Firms.')
    st.write(a.recommendations)
else: 
    st.write('.')

