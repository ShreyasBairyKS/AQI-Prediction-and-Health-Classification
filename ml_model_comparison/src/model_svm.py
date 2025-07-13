class SVMModel:
    def __init__(self):
        from sklearn.svm import SVC
        self.model = SVC(max_iter=1000)  # Increased max_iter

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)