#  https://www.runoob.com/sqlite/sqlite-python.html

import sqlite3

import pandas as pd

conn = sqlite3.connect('../../dbs/zkz.db')

df = pd.read_sql_query("SELECT * from ZC", conn)

conn.close()

print(df)
