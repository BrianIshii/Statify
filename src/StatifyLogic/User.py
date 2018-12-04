# User file
from src.DatabaseAccess import History


class User:
    def __init__(self, uid):
        self.id = uid
        self.history = History(uid)

    def get_trend(self, trend, start_time, end_time):
        data = self.history.get_data(start_time, end_time)
        return trend.find_trend(data)

    def get_recommendation(self, recommendation, start_time, end_time):
        data = self.history.get_data(start_time, end_time)
        return recommendation.find_recommendations(data)

    def store_trend(self, trend_name, data):
        self.history.store_trend(trend_name, data)

    def store_recommendation(self, recommendation_name, data):
        self.history.store_recommendation(recommendation_name, data)
