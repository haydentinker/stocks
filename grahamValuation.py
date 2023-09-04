import yfinance as yf
from get5YearGrowth import get5YearGrowthRate
from getCurrentYield import getCurrentYield

def grahamValuation(ticker):
    company = yf.Ticker(ticker)
    eps= float(company.info['trailingEps'])
    growthRate=get5YearGrowthRate(ticker)
    currentYield=getCurrentYield()
    result=(eps*(8.5+2*growthRate)*(4.4/currentYield))
    return(result)
