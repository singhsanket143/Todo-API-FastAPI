from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoModel(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True, nullable=True)
    completed = Column(Boolean, default=False)