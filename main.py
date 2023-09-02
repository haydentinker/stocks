from grahamValuation import grahamValuation
import yfinance as yf
def main():
    ticker=input("Enter ticker: ")
    marginOfSafety=float(input("Enter margin of Safety as decimal: "))
    company=yf.Ticker(ticker)
    currentPrice=company.info['currentPrice']
    print(f"Current Price: {currentPrice}")
    intrinsicValue=grahamValuation(ticker)
    print(f"Intrinsic Value: {intrinsicValue}")
    difference=currentPrice/intrinsicValue
    differencePercentage=round((difference*100),2)
    print(f"Difference: {differencePercentage}%")
    print(f'Acceptable Buy Price:{intrinsicValue*marginOfSafety} ')

if __name__ == "__main__":
    main()