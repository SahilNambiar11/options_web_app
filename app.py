import streamlit as st
import yfinance as yf
import visuals
from data_fetch import get_stock_data, get_options_chain
from datetime import date

# --- App Title ---
st.title("Options Strategy Simulator")

# --- Strategy Selection ---
strategies = ["Covered Call", "Protective Put"]
strategy_selection = st.sidebar.selectbox("Choose the strategy", strategies)

# --- Sidebar Inputs ---
st.sidebar.header("Enter Parameters")

# Ticker input
ticker_symbol = st.sidebar.text_input("Ticker", value="").strip()

# Date range input with try-except to avoid errors while selecting
try:
    date_range = st.sidebar.date_input(
        "Select a date range",
        value=[date(2024, 1, 1), date.today()]
    )
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = None
except Exception:
    start_date = end_date = None

# --- Validation ---
valid_inputs = False
if not ticker_symbol:
    st.warning("Please input a ticker symbol")
elif start_date is None or end_date is None:
    st.info("Select both start and end dates")
elif start_date > end_date:
    st.warning("Start date cannot be after end date")
else:
    # Fetch stock data
    data = get_stock_data(ticker_symbol, start_date, end_date)
    if data.empty:
        st.warning("No data available for this date range and ticker")
    else:
        valid_inputs = True
        # Set stock price to start-date closing price
        stock_price = float(data['Close'].iloc[0])
        st.sidebar.write(f"Stock Price on {start_date}: ${stock_price:.2f}")

# --- Show strategy-specific inputs only if valid ---
if valid_inputs:
    if strategy_selection == "Covered Call":
        call_strike = st.sidebar.number_input("Call Strike Price", value=stock_price * 1.05)
        call_premium = st.sidebar.number_input("Call Premium Received", value=5.0)
    elif strategy_selection == "Protective Put":
        put_strike = st.sidebar.number_input("Put Strike Price", value=stock_price * 0.95)
        put_premium = st.sidebar.number_input("Put Premium Paid", value=5.0)

    # --- Plot historical data ---
    visuals.plot_historical_data(data, ticker_symbol)

    # --- P/L Simulation ---
    if st.sidebar.button("Plot P/L Curve"):
        if strategy_selection == "Covered Call":
            st.write(f"Simulating Covered Call: Stock={stock_price}, Strike={call_strike}, Premium={call_premium}")
            visuals.plot_covered_call(stock_price, call_strike, call_premium)
        elif strategy_selection == "Protective Put":
            st.write(f"Simulating Protective Put: Stock={stock_price}, Strike={put_strike}, Premium={put_premium}")
            visuals.plot_protective_put(stock_price, put_strike, put_premium)

    # --- Options Chain ---
    try:
        stock = yf.Ticker(ticker_symbol)
        expirations = stock.options

        if expirations:
            selected_expiration = st.sidebar.selectbox(
                "Select option expiration", expirations
            )

            if selected_expiration:
                options_chain = get_options_chain(ticker_symbol, selected_expiration)

                filtered_chain = options_chain[
                    (options_chain['Call Bid'] > 0) |
                    (options_chain['Call Ask'] > 0) |
                    (options_chain['Put Bid'] > 0) |
                    (options_chain['Put Ask'] > 0)
                ]

                if filtered_chain.empty:
                    st.info("No active options found for this expiration.")
                else:
                    st.subheader(f"Options Chain for {ticker_symbol} expiring on {selected_expiration}")
                    st.dataframe(filtered_chain)
        else:
            st.info("No available option expirations for this ticker.")
    except Exception as e:
        st.warning(f"Could not fetch options chain: {e}")
