import tkinter as tk
import yfinance as yf
from grahamValuation import grahamValuation

def main():
    root = tk.Tk()
    root.title("Graham Valuation")
    root.geometry("500x500")

    # Create a StringVar to store the ticker symbol entered by the user
    ticker = tk.StringVar()

    tickerLabel = tk.Label(root, text="Ticker")
    tickerLabel.pack(side=tk.TOP, anchor=tk.NW)

    tickerEntry = tk.Entry(root, textvariable=ticker)
    tickerEntry.pack(side=tk.TOP, anchor=tk.NW)

    # Create a margin of safety entry field
    marginOfSafety = tk.DoubleVar()
    marginOfSafety.set(0.0)  # Set the initial value to 0.0

    marginLabel = tk.Label(root, text="Margin of Safety")
    marginLabel.pack(side=tk.TOP, anchor=tk.NW)

    marginEntry = tk.Entry(root, textvariable=marginOfSafety)
    marginEntry.pack(side=tk.TOP, anchor=tk.NW)
    submitButton = tk.Button(root, text="Submit", command=lambda: calculateAndPrint(root, ticker.get(), marginOfSafety.get()))
    submitButton.pack(side=tk.TOP, anchor=tk.NW)
    result_frame = tk.Frame(root)
    result_frame.pack(side=tk.TOP, anchor=tk.NW)
    root.mainloop()

def calculateAndPrint(root, ticker, marginOfSafety):
    for widget in root.winfo_children():
        if widget.winfo_parent() == root:
            widget.destroy()
    company = yf.Ticker(ticker)
    currentPrice = company.info['currentPrice']

    intrinsicValue = grahamValuation(ticker)
    difference = intrinsicValue / currentPrice
    differencePercentage = round((difference * 100), 2)

    resultLabel = tk.Label(root, text=f"Current Price: {currentPrice}")
    resultLabel.pack(side=tk.TOP, anchor=tk.NW)

    resultLabel = tk.Label(root, text=f"Intrinsic Value: {intrinsicValue}")
    resultLabel.pack(side=tk.TOP, anchor=tk.NW)

    resultLabel = tk.Label(root, text=f"Difference: {differencePercentage}%")
    resultLabel.pack(side=tk.TOP, anchor=tk.NW)

    acceptableBuyPrice = intrinsicValue * marginOfSafety
    resultLabel = tk.Label(root, text=f'Acceptable Buy Price: {acceptableBuyPrice}')
    resultLabel.pack(side=tk.TOP, anchor=tk.NW)

if __name__ == "__main__":
    main()
