from sklearn.ensemble import RandomForestRegressor

class RandomForestRegressorModel:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=30)
    def train(self, X, y):
        self.model.fit(X, y)
    def predict(self, X):
        return self.model.predict(X)