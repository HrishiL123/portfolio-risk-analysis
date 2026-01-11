from src.data import fetch_price_data
from src.metrics import compute_portfolio_metrics
from src.visualize import plot_prices, plot_risk_return
import pandas as pd
import matplotlib.pyplot as plt

prices = fetch_price_data(
    tickers=["AAPL", "MSFT", "GOOG"],
    start="2024-01-01",
    end="2025-12-31"
)

annual_return, annual_volatility, sharpe_ratio = compute_portfolio_metrics(prices)

metrics_df = pd.DataFrame({
    "Annual Return": annual_return,
    "Annual Volatility": annual_volatility,
    "Sharpe Ratio": sharpe_ratio
})

plot_prices(prices)
plot_risk_return(metrics_df["Annual Return"], metrics_df["Annual Volatility"], metrics_df["Sharpe Ratio"])

