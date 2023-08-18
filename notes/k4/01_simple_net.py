import random


# y = wx + b
# y_hat 是真实标签
# loss = (y - y_hat)^2 = (wx+b - y_hat)^2
# loss对 w = 2 * x * (wx + b - y_hat)
# loss对 b = 2  * (wx + b - y_hat)
class LinearModel():
    def __init__(self):
        self.w = random.random()
        self.b = random.random()

    def forward(self, x):
        y_pred = self.w * x + self.b
        return y_pred

    def backward(self, y, y_hat, xi, lr=0.01):
        self.w = self.w - lr * 2 * xi * (y - y_hat)
        self.b = self.b - lr * 2 * (y - y_hat)


lm = LinearModel()
print(lm.w)
print(lm.b)
x = [1, 2, 3, 4, 5]
y = [2.1, 4.1, 6.1, 8.1, 10.1]
for i in range(1000):
    for xi, y_hat_i in zip(x, y):
        yi = lm.forward(xi)
        lm.backward(yi, y_hat_i, xi)

print(lm.w)
print(lm.b)

print(lm.forward(5))
