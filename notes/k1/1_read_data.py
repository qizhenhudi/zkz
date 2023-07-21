# 下面这个代码有什么问题
# CTRL+ /
# with open("../../datas/1936/1月1日.txt") as f:
#     for l in f.readlines():
#         print(l)

# 列表

lines = []  # 创建空列表
with open("../../datas/1936/1月1日.txt", encoding="utf-8") as f:
    for l in f.readlines():
        lines.append(l)  # 往空列表依次增加元素
# print(lines)
#
# 读取文件夹下的所有文件名
import os

dir_list = os.listdir("../../datas/1936")
print(dir_list)
# ['1月1日.txt', '1月2日.txt', '1月3日.txt', '1月4日.txt', '1月5日.txt', '1月6日.txt', '1月7日.txt', '1月8日.txt']
#


# 拼接字符串
path = "../../datas/1936" + "/" + dir_list[0]
print(path)

#
# 如何读取上面所有文件的内容
diary_list = []
for file_name in dir_list:
    path = "../../datas/1936" + "/" + file_name
    lines = []  # 创建空列表
    with open(path, encoding="utf-8") as f:
        for l in f.readlines():
            lines.append(l)
        diary_list.append(lines)

print(diary_list)

# 列表推导
# 统计日记里多少段落
diary_statistic = [len(x) for x in diary_list]
print(diary_statistic)
#
# 统计每天写了多少字
diary_statistic_words = [sum([len(xi) for xi in x]) for x in diary_list]
print(diary_statistic_words)  # 这是准确的么？

diary_statistic_words = [sum([len(xi.replace(" ", "")) for xi in x]) for x in diary_list]
print(diary_statistic_words)

str = '回南京 雪\u3000\u3000\n'
print(str)
print(str.replace(" ", ""))
print(len(str.replace(" ", "")))
print(len(str.replace('\u3000', '').replace(" ", "").strip()))
#
# 字典  key  value
# 统计竺校长喜欢用哪些字，可以用key表示字，value表示数目
diary_count = {}

# 定义要删除的标点符号
punctuation = """!"#$%&'()〔〕。，、·《》°*+,-./:;<=>?@[\]^_`{|}~"""

import re
for diary in diary_list:
    for di in diary:
        di = di.replace('\u3000', '').replace(" ", "").strip()
        # 使用replace()方法删除标点符号
        for pi in punctuation:
            di = di.replace(pi, '')
        # di = "".join([i for i in di if not i.isalpha()]) # 这个无法去除字母
        di = "".join([i for i in di if not i.isnumeric()])  # 去除数字
        di = re.sub('[a-zA-Z0-9]','',di)  # 去除字母和数字
        for dij in di:
            if dij in diary_count.keys():
                diary_count[dij] = diary_count[dij] + 1
            else:
                diary_count.update({dij: 1})
print(diary_count)

# # 去除字母和数字
# print("张".isalpha())
# str_a = "张8a"
# str_a = re.sub('[a-zA-Z0-9]','',str_a)
# print(str_a)
