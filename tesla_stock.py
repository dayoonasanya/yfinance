import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'TSLA'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-01-01', end='2024-05-04')

# Print the data
print(tickerDf)
