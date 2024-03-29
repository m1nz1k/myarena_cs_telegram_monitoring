from sqlalchemy import Column, BigInteger, String, sql, DateTime
from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    active_token = Column(String(100))
    query: sql.select