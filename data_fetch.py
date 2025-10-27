import yfinance as yf
import pandas as pd

#function to get historical stock prices based on a ticker symbol
def get_stock_data(ticker, start, end):
    #downloads daily stock prices between 2 days
    data = yf.download(ticker, start=start, end=end)
    return data

#gets the options chain for a specific expiration date
def get_options_chain(ticker, expiration):
    #create a ticker object
    stock = yf.Ticker(ticker)
    #get teh calls and puts the option data for that expiration
    chain = stock.option_chain(expiration)

    calls = chain.calls
    puts = chain.puts

    chain_summary = pd.DataFrame({
        "Strike": calls['strike'],
        "Call Bid": calls['bid'],
        "Call Ask": calls['ask'],
        "Put Bid": puts['bid'],
        "Put Ask": puts['ask']
    })

    return chain_summary