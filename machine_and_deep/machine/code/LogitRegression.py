import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LogitRegression():
    def __init__(self):
        self.X = None
        self.y = None
        self.theta_init = None

    def cost(self,X, y, theta):
        left = np.multiply(-y, np.log(self.model(X, theta)))
        right = np.multiply(1 - y, np.log(1 - self.model(X, theta)))
        return np.sum(left - right) / (len(X))


    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def gradient(self,X, y, theta):
        grad = np.zeros(theta.shape)
        error = (self.model(X, theta) - y).ravel()
        for j in range(len(theta.ravel())):  # for each parmeter
            term = np.multiply(error, X[:, j])
            grad[0, j] = np.sum(term) / len(X)

        return grad

    def model(self, X, theta):
        return self.sigmoid(np.dot(X, theta.T))

    def shuffleData(self,data):
        np.random.shuffle(data)
        cols = data.shape[1]
        X = data[:, 0:cols - 1]
        y = data[:, cols - 1:]
        return X, y

    def predict(self,X):
        return [1 if x >= 0.5 else 0 for x in self.model(X, self.theta)]

    def insert_one(self,data):
        return np.insert(data, 0, 1, axis=1)

    def descent(self, data, theta, batchSize, thresh, alpha):
        i = 0  # 迭代次数
        k = 0  # batch
        # grad = np.zeros(theta.shape)  # 计算的梯度
        costs = [self.cost(self.X, self.y, theta)]  # 损失值
        while True:
            grad = self.gradient(self.X[k:k + batchSize], self.y[k:k + batchSize], theta)
            k += batchSize  # 取batch数量个数据
            if k >= batchSize:
                k = 0
                self.X, self.y = self.shuffleData(data)  # 重新洗牌
            theta = theta - alpha * grad  # 参数更新
            costs.append(self.cost(self.X, self.y, theta))  # 计算新的损失
            value = costs
            if abs(value[-1]-value[-2]) < thresh : break
        return theta, i - 1, costs, grad

    def fit(self,data, batchSize, thresh, alpha):
        data = self.insert_one(data)
        self.X,self.y = self.shuffleData(data)
        self.theta_init = np.zeros([1, self.X.shape[1]])
        self.theta, iter, costs, grad = self.descent(data, self.theta_init, batchSize, thresh, alpha)
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(np.arange(len(costs)), costs, 'r')
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Cost')
        ax.set_title('Error vs Iteration')
        plt.show()
        return self

if __name__ == '__main__':
    path = '../data/LogitRegression_data.txt'
    pdData = pd.read_csv(path, header=None, names=['X1', 'X2', 'lable'])
    orig_data = pdData.values
    cols = orig_data.shape[1]
    X = orig_data[:, 0:cols - 1]
    y = orig_data[:, cols - 1:cols]
    logitregression = LogitRegression()
    logitregression.fit(orig_data, 100, thresh=0.000001, alpha=0.001)

    print(logitregression.predict([[1,34.62365962451697,78.0246928153624]]))
