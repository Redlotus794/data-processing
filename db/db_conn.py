"""
数据库连接对象
"""
from sqlalchemy import create_engine

class DBConn:

    def __init__(self, conn):
        create_engine()
        self.conn = conn

