import yfinance as yf

yf.enable_debug_mode()

def search_tickers(query):
    data = yf.Tickers(query)
    return [
        {
            "symbol": t.info.get("symbol"),
            "shortName": t.info.get("shortName"),
            "marketPrice": t.info.get("regularMarketPrice"),
        } for t in data.tickers.values()
    ]

def get_quote(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    hist = ticker.history(period="1mo")
    return {
        "symbol": symbol,
        "price": info.get("regularMarketPrice"),
        "currency": info.get("currency"),
        "history": hist["Close"].reset_index().to_dict(orient="list"),
    }






















dat = yf.Ticker("MSFT")
dat = yf.Ticker("MSFT")
dat.info
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')
dat.option_chain(dat.options[0]).calls
spy = yf.Ticker('SPY').funds_data
print(spy.description)
print("------------------------------------------------")
print(spy.top_holdings)
print("------------------------------------------------")
print(yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo'))

