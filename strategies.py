def covered_call(stock_price, call_strike, call_premium, num_shares=100):
    #calculate maximum profit if stock finishes at or above strike
    max_profit = call_strike - stock_price + call_premium

    #maximum loss happens when the stock reaches 0
    max_loss = - stock_price + call_premium

    #breakeven happens when profit and loss = 0
    breakeven = stock_price - call_premium

    return max_profit, max_loss, breakeven

def protective_put(stock_price, put_strike, put_premium, num_shares=100):
    # Max loss: stock drops to 0, but put gives you strike - 0 protection
    max_loss = -(stock_price - put_strike + put_premium)
    
    # Max profit: unlimited on the upside (theoretically infinite)
    # But we can approximate by showing potential gain up to some stock price range
    max_profit = "Unlimited"

    # Breakeven happens when profit = 0
    breakeven = stock_price + put_premium

    return max_profit, max_loss, breakeven


