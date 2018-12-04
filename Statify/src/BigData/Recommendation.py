
class Recommendation:
    def __init__(self, strategy, train_data):
        self.strategy = strategy
        self.train_data = train_data
        self.items = []

    def find_recommendations(self, test_data):
        self.strategy.train(self.train_data)
        return self.strategy.test(test_data)