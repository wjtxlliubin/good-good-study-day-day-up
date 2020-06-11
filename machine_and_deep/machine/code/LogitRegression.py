import numpy as np
import pandas as pd

class LogitRegression():
    def __init__(self, X,y,thresh):
        self.X = X
        self.y = y
        self.thresh = thresh

    def cost(self,X, y, theta):
        left = np.multiply(-y, np.log(self.model(X, theta)))
        right = np.multiply(1 - y, np.log(1 - self.model(X, theta)))
        return np.sum(left - right) / (len(X))

    def fit(self, X, y):
        # 定义初始0向量参数，参数个数同X的特征数，维度为(1,X.shape[1])
        self.coef_ = np.zeros(shape=(1, X.shape[1]))
        # 初始截距维度为1
        self.intercept_ = np.zeros(1)
        # 初始化cost
        self.cost_ = []

        if not self.cost: raise Exception('cost is None')
        cost = float('INF')
        while cost > self.thresh:
            cost = self.handle(X,y)
        return self

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
        # np.dot相当于矩阵乘法，[x的样本数，x的特征数]*[参数维度，1]，结果等于[x的样本对应的预测值，1]

        return self.sigmoid(np.dot(X, theta.T))

    def shuffleData(self,data):
        np.random.shuffle(data)
        cols = data.shape[1]
        X = data[:, 0:cols - 1]
        y = data[:, cols - 1:]
        return X, y

    def predict(self, X):
        return self.net_input(X)

    def descent(self,data, theta, batchSize, stopType, thresh, alpha):
        # 梯度下降求解

        i = 0  # 迭代次数
        k = 0  # batch
        grad = np.zeros(theta.shape)  # 计算的梯度
        costs = [self.cost(self.X, self.y, theta)]  # 损失值
        n = 100
        while True:
            grad = self.gradient(X[k:k + batchSize], y[k:k + batchSize], theta)
            k += batchSize  # 取batch数量个数据
            if k >= n:
                k = 0
                X, y = self.shuffleData(data)  # 重新洗牌
            theta = theta - alpha * grad  # 参数更新
            costs.append(self.cost(X, y, theta))  # 计算新的损失
            i += 1


            value = costs

            if abs(value[-1]-value[-2]) < thresh : break

        return theta, i - 1, costs, grad

if __name__ == '__main__':
    import os
    path = '../data/LogiReg_data.txt'
    pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
    print(pdData.head())
    orig_data = pdData.as_matrix()  # convert the Pandas representation of the data to an array useful for further computations
    cols = orig_data.shape[1]
    X = orig_data[:, 0:cols - 1]
    y = orig_data[:, cols - 1:cols]

    # convert to numpy arrays and initalize the parameter array theta
    # X = np.matrix(X.values)
    # y = np.matrix(data.iloc[:,3:4].values) #np.array(y.values)
    theta = np.zeros([1, 3])
