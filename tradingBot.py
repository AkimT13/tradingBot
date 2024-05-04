from lumibot.brokers import Alpaca
from lumibot.strategies.strategy import Strategy
from lumibot.backtesting import YahooDataBacktesting, BacktestingBroker
from lumibot.traders import Trader
from datetime import datetime
import requests

API_KEY = "PK9B9P3CI1O72LDKA2VY"
API_SECRET = "ex09AVsmfa4uV3gSJrQZQR1RweZ5xxzm6NCBened"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CONFIG = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}




class MyStrategy(Strategy):
    # Custom parameters
    parameters = {
        "symbol": "SPY",
        "quantity": 1,
        "side": "buy"
    }



    def initialize(self, symbol=""):
        # Will make on_trading_iteration() run every 180 minutes
        self.sleeptime = "180M"

    def on_trading_iteration(self):
        symbol = self.parameters["symbol"]
        quantity = self.parameters["quantity"]
        side = self.parameters["side"]

        order = self.create_order(symbol, quantity, side)
        self.submit_order(order)


trader = Trader()
broker = Alpaca(ALPACA_CONFIG)
strategy = MyStrategy(name="strat", budget=100000, broker=broker, symbol="SPY")
backtesting_start = datetime(2020, 1, 1)
backtesting_end = datetime(2020, 12, 31)
strategy.backtest(
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
    parameters= {
        "symbol": "SPY"
    },
)
trader.add_strategy(strategy)
trader.run_all()
a = 5
