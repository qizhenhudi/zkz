#  https://www.runoob.com/sqlite/sqlite-python.html

import sqlite3

conn = sqlite3.connect('../../dbs/zkz.db')
print("成功打开数据库")

c = conn.cursor()
c.execute('''
       CREATE TABLE ZC
       (ID            INTEGER PRIMARY KEY   AUTOINCREMENT,
       WORD           CHAR(100)    NOT NULL,
       COUNT        INT NOT NULL);'''
          )
conn.commit()  # 提交事务
print("数据表创建成功")
conn.close()
