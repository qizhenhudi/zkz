# CTRL+ALT+L 代码格式
# 读取文件夹下的所有文件名
import os

dir_list = os.listdir("../../datas/1936")

# 如何读取上面所有文件的内容
diary_list = []
for file_name in dir_list:
    path = "../../datas/1936" + "/" + file_name
    lines = []  # 创建空列表
    with open(path, encoding="utf-8") as f:
        for l in f.readlines():
            lines.append(l)
        diary_list.append(lines)

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
        di = re.sub('[a-zA-Z0-9]', '', di)  # 去除字母和数字
        for dij in di:
            if dij in diary_count.keys():
                diary_count[dij] = diary_count[dij] + 1
            else:
                diary_count.update({dij: 1})
print(diary_count)

# 如何把上面的内容存储起来，比如CSV，在存储之前我们先了解python的数据框结构，可以看作类似的CSV


import pandas as pd

df = pd.DataFrame(columns=["word", "count"])  # 首先创建一个空的数据框，已经把列名设置好了，接下来就是加载数据
print(df)

for k, v in diary_count.items():
    # df = df.append({"word":k,"count":v},ignore_index=True) # FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
    df = pd.concat([df, pd.DataFrame({"word": [k], "count": [v]})])

print(df)

df.to_csv("../../outputs/zkz/diary_count.csv", index=False, encoding="gb18030")
