import numpy as np


class LinearRegression():
    def __init__(self, eta, cost=None, iter=None, iter_or_cost="iter"):
        self.iter = iter
        self.eta = eta
        self.cost = cost
        self.iter_or_cost = iter_or_cost

    def fit(self, X, y):
        # 定义初始0向量参数，参数个数同X的特征数，维度为(1,X.shape[1])
        self.coef_ = np.zeros(shape=(1, X.shape[1]))
        # 初始截距维度为1
        self.intercept_ = np.zeros(1)
        # 初始化cost
        self.cost_ = []

        if self.iter_or_cost == 'cost':
            if not self.cost: raise Exception('cost is None')
            cost = float('INF')
            while cost > self.cost:
                cost = self.handle(y)
        elif self.iter_or_cost == 'iter':
            if not self.iter: raise Exception('iter is None')
            # 迭代循环
            for i in range(self.iter):
                self.handle(y)
        else:
            raise Exception('iter_or_cost is None')

        return self

    def handle(self, y):

        output = self.net_input(X)

        errors = y - output
        # 参数更新，等于旧参数+学习率*预测误差*，矩阵乘法上，[1，x的样本对应的误差]*[x的样本数，x的特征数]=[1,x的特征数对应的更新值]
        self.coef_ += self.eta * np.dot(errors.T, X)
        # 截距更新=截距旧值+学习率*误差总和
        self.intercept_ += self.eta * errors.sum()
        # 误差平方和，即损失函数
        cost = (errors ** 2).sum() / 2.0
        # 保存误差平方和
        self.cost_.append(cost)

        return cost

    def net_input(self, X):
        # np.dot相当于矩阵乘法，[x的样本数，x的特征数]*[参数维度，1]，结果等于[x的样本对应的预测值，1]
        return np.dot(X, self.coef_.T) + self.intercept_

    def predict(self, X):
        return self.net_input(X)


if __name__ == '__main__':
    X = np.array([[1], [2], [3], [4], [5], [6]])
    print(X.shape)
    Y = np.array([[2], [4], [6], [8], [10], [12]])
    linear_regression = LinearRegression(0.001, cost=0.01, iter_or_cost="cost")
    linear_regression.fit(X, Y)
    print(linear_regression.predict([[7]]))
