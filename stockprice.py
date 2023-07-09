import streamlit as st
import yfinance as fn

#st.write("hello")

def get_ticker(name):
    company = fn.Ticker(name)
    return company
c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")

#Fetching data for dataframe
apple = fn.download("AAPL",start="2010-11-11", end="2021-11-11")
microsoft = fn.download("MSFT",start="2010-11-11", end="2021-11-11")
tesla = fn.download("TSLA",start="2010-11-11", end="2021-11-11")

#Fetching historical data by valid periods
data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c3.history(period="3mo")

#Markdown
st.write("""### APPLE""")
#Detailed summary about Apple
st.write(c1.info['longBusinessSummary'])
#Dataframe
st.write(apple)
#Chart
st.line_chart(data1.values)

st.write("""### MICROSOFT""")
st.write(c2.info['longBusinessSummary'])
st.write(microsoft)
st.line_chart(data2.values)

st.write("""### TESLA""")
st.write(c3.info['longBusinessSummary'])
st.write(tesla)
st.line_chart(data3.values)