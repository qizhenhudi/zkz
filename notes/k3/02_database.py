import sqlite3
import pandas as pd
from utils.db.sqlite3_util import Sqlite3Tool

# 数据库的创建

#  创建数据库的格式如下
# CREATE TABLE database_name.table_name(
#    column1 datatype  PRIMARY KEY(one or more columns),
#    column2 datatype,
#    column3 datatype,
#    .....
#    columnN datatype,
# );

sqlite3_tool = Sqlite3Tool(db_path="../../dbs/zkz.db")

# 查询语句
# SELECT column1, column2, columnN FROM table_name WHERE ...;

select_sql = "select * from ZC"
df = sqlite3_tool.execute_select_sql(select_sql)
print(df)

# 插入语句

# INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]
# VALUES (value1, value2, value3,...valueN);

word = "启"
count = 805
insert_sql = f"""INSERT INTO ZC(WORD,COUNT) VALUES ("{word}",{count})"""
print(insert_sql)
sqlite3_tool.execute_sql(insert_sql)
df = sqlite3_tool.execute_select_sql(select_sql)
print(df.tail())

# 更新语句
# UPDATE table_name
# SET column1 = value1, column2 = value2...., columnN = valueN
# WHERE [condition];
update_sql = f"""UPDATE ZC SET COUNT = 905 WHERE WORD = '启'"""  # 如果WORD是启就把COUNT更新为905
print(update_sql)
sqlite3_tool.execute_sql(update_sql)
df = sqlite3_tool.execute_select_sql(select_sql)
print(df.tail())
