from sqlalchemy import Column, Integer, String, Text, DateTime

from database import BaseModel
import datetime as dt


class Log(BaseModel):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, nullable=False, default=dt.datetime.now)
    name = Column(Text, nullable=False)
    priority = Column(String(20), nullable=True)
    message = Column(Text, index=True)
