from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, echo=True)

LocalSession = sessionmaker(bind=engine)

async def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
