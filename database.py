
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

# URL encode the password to handle special characters
password = quote("Mysql17?", safe="")
db_url = f"mysql+pymysql://root:{password}@localhost:3306/inventory_db"
engine = create_engine(db_url, pool_pre_ping=True, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
