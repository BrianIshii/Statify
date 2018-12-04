
class Recommendation:
    def __init__(self, strategy, trainData):
        self.strategy = strategy
        self.trainData = trainData

    def findRecommendations(self, testData):
        self.strategy.train(self.trainData)
        return self.strategy.test(testData)