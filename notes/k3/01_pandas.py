import pandas as pd

#################  Series  ################

#  Series是一维标记数组，可以存储不同类型的数据。

# 创建一个包含不同类型数据的Series
data = [10, '晨六点一刻', 3.14, True]
series = pd.Series(data)
print(series)
print(series.dtypes)

for s in series:
    print(s)
    print(type(s))

#################  pandas  ################
# DataFrame数据框是二维结构，可以看成表格，类似csv。
# 创建数据框
data = {
    'name': ['张三', '李四', '王老五', "刘六"],
    'age': [25, 30, 35, 28],
    'year_2022': [3, 1, 2, 4],
    'year_2023': [1, 3, 2, 4],
    'a_2023_b': [8, 5, 9, 6]
}

df = pd.DataFrame(data)
print(df)

#################  数据选择过滤 对列 ################
# 选择某一列
name = df['name']
print(name)  # 选择一列是series

# 选择多列
selected_columns = df[['name', 'age']]
print(selected_columns)  # 选择多列是DataFrame

# 选择列名以"year_"开头的列
filtered_columns = df.filter(like='year_')
print(filtered_columns)

# 选择列名包含"2023"的列
print("-------")
filtered_columns = df.filter(like='2023')
print(filtered_columns)

# 选择列名以"2023"结尾的列
print("-------")
filtered_columns = df.filter(like='_2023')  # 有问题，为何？
print(filtered_columns)

# 选择列名以"2023"结尾的列
print("-------")
filtered_columns = df.filter(regex='2023$')
print(filtered_columns)

#################  数据选择过滤 对行 ################

# 根据条件过滤数据
filtered_data = df[df['age'] > 30]
print(filtered_data)

# 使用.loc[]方法同时进行行和列过滤
filtered_data = df.loc[df['age'] > 27, ['name', 'age']]
print(filtered_data)

#################  loc和iloc ################
filtered_data = df.loc[1:2, ['name', 'age']]
# filtered_data = df.iloc[1:2, ['name', 'age']] 报错 .iloc使用标签索引进行数据选择
print(filtered_data)

# 使用.iloc[]方法同时进行行和列选择
filtered_data = df.iloc[1:2, [0, 1]]
# filtered_data = df.iloc[1:2, ['name', 'age']]  报错 .iloc使用整数索引来选择行和列
print(filtered_data)
