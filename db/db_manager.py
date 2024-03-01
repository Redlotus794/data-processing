"""
数据库连接对象
"""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from config.settings import Settings


class DBConn:
    """
    数据库连接对象
    """

    def __init__(self):
        """
        初始化
        """
        self.engine = create_engine(Settings.DB_URL, echo=bool(Settings.DEBUG))
        self.session = sessionmaker(bind=self.engine)()

    def insert(self, model):
        """
        插入
        :param model:Base
        :return: None
        """
        self.session.add(model)
        self.session.commit()

    
    def delete_all(self, model):
        """
        删除所有数据
        """
        self.session.execute(delete(model))
        self.session.commit()
    

    def close(self):
        """
        关闭
        :return: None
        """
        self.session.close()
        self.engine.dispose()

    def merge(self, model):
        """
        插入或更新
        """
        self.session.merge(model)
        self.session.commit()

    def execute(self, stmt):
        """
        执行statment
        """
        self.session.execute(stmt)
        self.session.commit()
