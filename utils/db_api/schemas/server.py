from sqlalchemy import Column, BigInteger, Sequence, String, sql

from utils.db_api.db_gino import  TimedBaseModel

class Server(TimedBaseModel):
    __tablename__ = 'servers'
    id = Column(BigInteger, Sequence('server_id_seq'), primary_key=True)
    server_name = Column(String(128))
    server_token = Column(String(128))

    query: sql.select