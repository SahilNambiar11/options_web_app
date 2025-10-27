# test_data_fetch.py (temporary test file)

from data_fetch import get_stock_data, get_options_chain

data = get_stock_data("AAPL", "2025-01-01", "2025-10-01")
calls, puts = get_options_chain("AAPL", "2025-10-17")

print(data.head())  # shows first 5 rows of stock data
print(calls.head()) # shows first 5 rows of call options
