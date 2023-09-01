import yfinance as yf
# data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
aapl = yf.Ticker("aapl")
print(aapl.info['discountRate'])