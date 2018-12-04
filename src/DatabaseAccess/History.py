class History:
    def __init__(self, id):
        self.id = id

    # returns all data for a time period
    def get_data(self, start_date, end_date):
        pass

    # returns all the data
    def get_all_data(self):
        pass

    # returns stored trends based of dates
    def get_trends(self, start_date, end_date):
        pass

    # returns all trends
    def get_all_trends(self):
        pass

    def store_trend(self, trend_name, data):
        pass

    def store_recommendation(self, recommendation_name, data):
        pass
