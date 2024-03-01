"""
Project Dragon的知识库的持久层Model对象
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
TABLE_ARGS = {'schema': 'p_dragon'}


class DragonKnowledgeBase(Base):
    """
    知识库持久层model对象
    """
    __tablename__ = 'dragon_knowledge_base'
    __table_args__ = TABLE_ARGS

    # id，自增长
    id = Column(Integer, primary_key=True)
    # hash值，文件hash，用以判断是否存在变更
    hash = Column(String, unique=True)
    # 文件的名称，全局唯一
    name = Column(String, unique=True)
    # 文件的内容
    content = Column(Text)
    # 创建时间
    create_time = Column(DateTime, default=datetime.datetime.now)