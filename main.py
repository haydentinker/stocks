import tkinter as tk
import yfinance as yf
from grahamValuation import grahamValuation

def main():
    root = tk.Tk()
    root.title("Graham Valuation Calculator")
    root.geometry("500x500")

    title_label=tk.Label(root,text='Graham Valuation Calculator',font='Calibri 24 bold')
    title_label.pack()
    
    input_frame=tk.Frame(root)
    # Setting up frame for ticker input 
    ticker = tk.StringVar()
    ticker.set("AAPL")
    ticker_frame=tk.Frame(input_frame)
    tickerLabel = tk.Label(ticker_frame, text="Ticker",font='Calibri 13')
    tickerLabel.pack()
    tickerEntry = tk.Entry(ticker_frame, textvariable=ticker)
    tickerEntry.pack()
    ticker_frame.pack(pady=10)
    
    #Setting up frame for margin of safety input
    marginSafety_frame=tk.Frame(input_frame)
    marginOfSafety_val = tk.DoubleVar()
    marginOfSafety_val.set(0.0)  
    marginLabel = tk.Label(marginSafety_frame, text="Margin of Safety",font='Calibri 13')
    marginLabel.pack()
    marginEntry = tk.Entry(marginSafety_frame, textvariable=marginOfSafety_val)
    marginEntry.pack()
    marginSafety_frame.pack(pady=10)

    #Result frame for calculations
    result_frame=tk.Frame(root)
    submitButton = tk.Button(input_frame, text="Submit", command=lambda: calculateAndPrint(result_frame, ticker.get(), marginOfSafety_val.get()),font='Calibri 13 bold')
    submitButton.pack(pady=10)
    input_frame.pack(pady=10)
    result_frame.pack(pady=10)

    root.mainloop()

def calculateAndPrint(root, ticker, marginOfSafety):
    for widget in root.winfo_children():
        widget.destroy()
    company = yf.Ticker(ticker)
    currentPrice = company.info['currentPrice']

    intrinsicValue = round(grahamValuation(ticker),2)
    difference = intrinsicValue / currentPrice
    differencePercentage = round((difference * 100), 2)
    nameLabel = tk.Label(root, text=f"Name: {company.info['longName']}",font='Calibri 18')
    nameLabel.pack(side=tk.TOP, anchor=tk.NW)

    currentPrice_Label = tk.Label(root, text=f"Current Price: {currentPrice}",font='Calibri 18')
    currentPrice_Label.pack(side=tk.TOP, anchor=tk.NW)

    intrinsicValue_Label = tk.Label(root, text=f"Intrinsic Value: {intrinsicValue}",font='Calibri 18')
    intrinsicValue_Label.pack(side=tk.TOP, anchor=tk.NW)

    differencePercent_Label = tk.Label(root, text=f"Difference: {differencePercentage}%",font='Calibri 18')
    differencePercent_Label.pack(side=tk.TOP, anchor=tk.NW)

    acceptableBuyPrice = intrinsicValue * marginOfSafety
    acceptableBuyPrice_Label = tk.Label(root, text=f'Acceptable Buy Price: {acceptableBuyPrice}',font='Calibri 18')
    acceptableBuyPrice_Label.pack(side=tk.TOP, anchor=tk.NW)

if __name__ == "__main__":
    main()
