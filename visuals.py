import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from strategies import covered_call
from strategies import protective_put

def plot_covered_call(stock_price, call_strike, call_premium):
    prices = list(range(int(stock_price*0.5), int(stock_price*1.5)+1))

    pl_values = []
    for price in prices:
        max_profit, max_loss, breakeven = covered_call(stock_price, call_strike, call_premium)

        if price >= call_strike:
            pl = max_profit
        else:
            pl = price - stock_price + call_premium

        pl_values.append(pl)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=prices,
        y=pl_values,
        mode='lines',
        name='Covered Call P/L'
    ))

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="black",
        annotation_text="Break-even",
        annotation_position="bottom right"
    )

    fig.update_layout(
        title="Covered Call Profit/Loss Curve",
        xaxis_title="Stock Price at Expiration",
        yaxis_title="Profit / Loss ($)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_historical_data(data, ticker):
    if data.empty:
        st.warning("No data available for this date range and ticker")
    
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
    
    fig = px.line(
        data,
        x=data.index,
        y="Close",
        title=f"{ticker} Historical Closing Prices",
        labels={"Close": "Price (USD)", "index": "Date"}
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_protective_put(stock_price, put_strike, put_premium):
    prices = list(range(int(stock_price*0.5), int(stock_price*1.5)+1))

    max_profit, max_loss, breakeven = protective_put(stock_price, put_strike, put_premium)
    pl_values = []

    for price in prices:
        stock_pl = price - stock_price
        put_pl = max(put_strike - price, 0)
        total_pl = stock_pl + put_pl - put_premium

        pl_values.append(total_pl)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=prices,
        y=pl_values,
        mode='lines',
        name='Protective Put P/L'
    ))

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="black",
        annotation_text=f"Break-even: ${breakeven:.2f}",
        annotation_position="bottom right"
    )
            
    fig.update_layout(
        title="Protective Put Profit/Loss Curve",
        xaxis_title="Stock Price at Expiration",
        yaxis_title="Profit / Loss ($)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)