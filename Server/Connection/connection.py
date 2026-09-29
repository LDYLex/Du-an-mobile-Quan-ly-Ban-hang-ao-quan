from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase
from sqlalchemy import create_engine
from dotenv import load_dotenv 
import os
load_dotenv()
url=os.getenv("url")
if not url:
    raise ValueError("khong tim thay bien url")
eng=create_engine(
url
)
try: 
    with  eng.connect(): 
        print("ket noi thanh cong")
except Exception as e: 
    print("ket noi that bai")
class Base(DeclarativeBase):
    pass
Se=sessionmaker(
     bind=eng,
     autoflush=False,
     autocommit=False
)
def get_db(): 
    db=Se()
    try: 
        yield db
    finally:
        db.close()