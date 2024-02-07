"""
数据库连接对象
"""
from sqlalchemy import create_engine
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

    def close(self):
        """
        关闭
        :return: None
        """
        self.session.close()
        self.engine.dispose()