"""
Schema GPT Builder
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_ARGS = {'schema': 'gptb'}


class BasicInfo(Base):
    """
    基础信息表
    """
    __tablename__ = 'basic_info'
    __table_args__ = TABLE_ARGS

    id = Column(Integer, primary_key=True)
    comment = Column(String)