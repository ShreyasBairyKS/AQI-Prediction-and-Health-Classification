from sklearn.svm import SVR

class SVMRegressorModel:
    def __init__(self):
        self.model = SVR()
    def train(self, X, y):
        self.model.fit(X, y)
    def predict(self, X):
        return self.model.predict(X)