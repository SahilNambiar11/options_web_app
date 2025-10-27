from strategies import covered_call

max_profit, max_loss, breakeven = covered_call(
    stock_price=150,
    call_strike=160,
    call_premium=5
)

print("Max Profit: ", max_profit)
print("Max Loss: ", max_loss)
print("Max Breakeven: ", breakeven)