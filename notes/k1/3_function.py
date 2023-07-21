
def my_read_line(file_path):
    lines = []  # 创建空列表
    with open(file_path, encoding="utf-8") as f:
        for l in f.readlines():
            lines.append(l)  # 往空列表依次增加元素
    return  lines

print(my_read_line(file_path= "../../datas/1936/1月1日.txt"))


