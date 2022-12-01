from sqlalchemy import create_engine
from configs.environment import Environment
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(Environment.get_db_url())
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()


Base = declarative_base()
