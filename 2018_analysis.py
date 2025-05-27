# Analyse 2018 data

import yfinance as YahooFinance

spy_data_year_2018 = YahooFinance.download("SPY", start = "start=2018-01-01", end="2018-12-31")

spy_data_year_2018.head()