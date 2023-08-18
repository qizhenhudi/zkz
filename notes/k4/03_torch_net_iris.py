import torch
import torch.nn as nn
import pandas as pd

iris_data = pd.read_csv("../../datas/Rdata/iris.csv")
print(iris_data.head())

data_x = torch.from_numpy(iris_data[:50][["Sepal.Length", "Sepal.Width", "Petal.Width"]].values).float()
print(data_x[:5])
data_y = torch.from_numpy(iris_data[:50][["Petal.Length"]].values).float()
print(data_y[:5])


class LinearModel(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, x):  # 必须要有forward函数
        y_pred = self.linear(x)  # 生成预测y_pred值
        return y_pred


model = LinearModel(3, 1)  # 实例化模型
criterion = torch.nn.MSELoss(size_average=True)  # 损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)  # 优化器

for epoch in range(1000):
    y_pred = model(data_x)  # 调用forward前向传播
    loss = criterion(y_pred, data_y)  # 获取损失函数
    if epoch % 100 == 0:
        print(f'''epoch = {epoch}, loss = {loss.item()}''')
    optimizer.zero_grad()  # 清除上次的梯度值
    loss.backward()  # 反向传播
    optimizer.step()  # 权重更新

print("w = ", model.linear.weight.detach().numpy())
print("b = ", model.linear.bias.detach().numpy())

x_test = torch.Tensor([4.9, 3, 0.2])
y_test = model(x_test)
print("y_pred = ", y_test.data.item())
