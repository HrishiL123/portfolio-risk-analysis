import matplotlib.pyplot as plt

def plot_prices(prices):
   
    prices.plot(figsize=(12, 6))
    plt.title("Stock Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price ($)")
    plt.grid(True)
    plt.show()


def plot_risk_return(annual_return, annual_volatility, sharpe_ratio):
   
    import numpy as np

    tickers = annual_return.index
    x = annual_volatility.values
    y = annual_return.values
    size = sharpe_ratio.values * 100  # scale for visualization

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=size, alpha=0.6)
    
    for i, ticker in enumerate(tickers):
        plt.text(x[i], y[i], ticker)

    plt.xlabel("Annualized Volatility (Risk)")
    plt.ylabel("Annualized Return")
    plt.title("Risk vs Return Scatter Plot (size = Sharpe ratio)")
    plt.grid(True)
    plt.show()
