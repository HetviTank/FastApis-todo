from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class todo_list(Base):

    __tablename__ = "Todo_List"
    id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, nullable=False
    )
    title = Column(String(50), index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)


class log_in(Base):

    __tablename__ = "log_in"

    email = Column(String(50), index=True, nullable=False, primary_key=True)
    password = Column(String(50), index=True, nullable=False)


class work_to_done(Base):

    __tablename__ = "work_to_done"

    id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, nullable=False
    )
    work_topic = Column(String(50), nullable=False)
    working_hr = Column(Integer, nullable=False)


user = relationship("log_in", backref="work_to_done")
