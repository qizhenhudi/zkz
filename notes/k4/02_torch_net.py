import torch
import torch.nn as nn


class LinearModel(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, x):  # 必须要有forward函数
        y_pred = self.linear(x)  # 生成预测y_pred值
        return y_pred


model = LinearModel(1, 1)  # 实例化模型
criterion = torch.nn.MSELoss(size_average=False)  # 损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 优化器

x = [1, 2, 3, 4, 5]
y = [2.1, 4.1, 6.1, 8.1, 10.1]
data_x = torch.tensor(x, dtype=torch.float).unsqueeze(1)
print(data_x)
data_y = torch.tensor(y).unsqueeze(1)
print(data_y)

for epoch in range(1000):
    y_pred = model(data_x)  # 调用forward前向传播
    loss = criterion(y_pred, data_y)  # 获取损失函数
    if epoch % 100 == 0:
        print(f'''epoch = {epoch}, loss = {loss.item()}''')
    optimizer.zero_grad()  # 清除上次的梯度值
    loss.backward()  # 反向传播
    optimizer.step()  # 权重更新

print("w = ", model.linear.weight.item())
print("b = ", model.linear.bias.item())

x_test = torch.Tensor([5.])
y_test = model(x_test)
print("y_pred = ", y_test.data.item())
