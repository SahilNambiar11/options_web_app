## License
This project is proprietary and all rights are reserved by the author.

#Options Strategy Simulator

An interactive web app built with **Streamlit** that allows users to **simulate options trading strategies** such as *Covered Calls* and *Protective Puts*.  
Users can view **historical stock data**, analyze **profit/loss curves**, and explore **live options chain data** fetched via Yahoo Finance.

---

## Features

- **Simulate Covered Calls & Protective Puts**
- **Interactive Profit/Loss Charts** using Plotly
- **View Historical Stock Data** via Yahoo Finance
- **Access Live Options Chain Data** with expiration filters
- **Streamlit-based UI** for quick parameter tuning and visualization

---

## How It Works

1. Enter a **ticker symbol** (e.g., `AAPL`, `TSLA`, `MSFT`)
2. Choose a **date range** for historical data
3. Select your **options strategy**
4. Enter the **strike price** and **premium**
5. Click **"Plot P/L Curve"** to visualize potential profit and loss
6. Optionally, view the **live options chain** for real-world pricing

---

## Project Structure

options_web_app/
│
├── app.py # Main Streamlit application
├── data_fetch.py # Functions for fetching stock & option data
├── strategies.py # Logic for trade simulation and payoff computation
├── visuals.py # Plotting and chart generation
├── test_*.py # Unit tests for modules
└── README.md # Project documentation
