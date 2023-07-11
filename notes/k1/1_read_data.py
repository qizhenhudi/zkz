
# 下面这个代码有什么问题
# with open("../../datas/1936/1月1日.txt") as f:
#     for l in f.readlines():
#         print(l)


with open("../../datas/1936/1月1日.txt", encoding="utf-8") as f:
    for l in f.readlines():
        print(l)


# 列表

lines = []  # 创建空列表
with open("../../datas/1936/1月1日.txt", encoding="utf-8") as f:
    for l in f.readlines():
        lines.append(l) # 往空列表依次增加元素

print(lines)

