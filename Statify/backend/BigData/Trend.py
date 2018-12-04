#BigData.py

class Trend:
    def __init__(self, strategy):
        self.strategy = strategy
        self.items = []

    def findTrend(self, songs):
        return self.strategy.findTrend(songs)