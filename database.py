from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base




DATABASE_URL = (
    f"postgresql://postgres:"
    f"vaib%401603@"
    f"localhost:"
    f"5432/"
    f"my_db"
)


engine =create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False , autocommit=False , bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()