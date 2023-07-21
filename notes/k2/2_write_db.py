#  https://www.runoob.com/sqlite/sqlite-python.html

import sqlite3

import pandas as pd

conn = sqlite3.connect('../../dbs/zkz.db')

df = pd.read_csv("../../outputs/zkz/diary_count.csv", encoding="gb18030")

# df.to_sql('ZKZ', conn, if_exists='replace', index=False)

df.to_sql('ZC', conn, if_exists='append', index=False)

conn.close()

# conn = sqlite3.connect('../../dbs/zkz.db')
# print("成功打开数据库")
#
# c = conn.cursor()
# c.execute('''
#        CREATE TABLE ZKZ
#        (ID            INT     PRIMARY KEY     NOT NULL,
#        NAME           CHAR(100)    NOT NULL,
#        TIME            DATETIME     NOT NULL,
#        CONTENT        TEXT NOT NULL);'''
#           )
# conn.commit()   # 提交事务
# print("数据表创建成功")
# conn.close()
