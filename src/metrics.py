def compute_portfolio_metrics(prices, risk_free_rate=0.02):
   
    # 1. Daily returns
    daily_returns = prices.pct_change().dropna()

    # 2. Annualized return
    annual_return = daily_returns.mean() * 252

    # 3. Annualized volatility
    annual_volatility = daily_returns.std() * (252 ** 0.5)

    # 4. Sharpe ratio
    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

    return annual_return, annual_volatility, sharpe_ratio
