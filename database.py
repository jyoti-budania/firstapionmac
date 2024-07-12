from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base


URL_DATABASE = 'postgresql://postgres:2207@localhost:5432/demo'


engine =create_engine(URL_DATABASE)

SessioLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

