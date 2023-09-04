import yfinance as yf
from get5YearGrowth import get5YearGrowthRate
from getCurrentYield import getCurrentYield

def grahamValuation(ticker):
    company = yf.Ticker(ticker)
    eps= float(company.info['trailingEps'])
    print(f"EPS:{eps}")
    growthRate=get5YearGrowthRate(ticker)
    print(f"Growth Rate:{growthRate} ")
    currentYield=getCurrentYield()
    print(f"Current Yield: {currentYield}")
    result=(eps*(8.5+2*growthRate)*(4.4/currentYield))
    return(result)
