import sqlite3
import pandas as pd
from sqlalchemy import create_engine


class Sqlite3Tool():
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite:///{db_path}")

    def execute_select_sql(self, sql):  # 对于select可以专门用pandas直接返回数据框
        df = pd.read_sql_query(sql, self.engine.raw_connection())
        return df

    def execute_sql(self, sql):
        try:
            conn = self.engine.raw_connection()  # 从连接池拿到一个连接
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()  # 提交事务
        except Exception as e:
            print(e)
            conn.rollback()  # 回滚事务
            return False
        finally:
            cursor.close()
            conn.close()
