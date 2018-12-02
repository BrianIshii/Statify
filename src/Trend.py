#Trend.py

class Trend:
    def __init__(self, strategy):
        self.strategy = strategy

    def findTrend(self, songs):
        return self.strategy.findTrend()
