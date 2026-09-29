from jose import jwt 
from dotenv import load_dotenv
import os 
from sqlalchemy.orm import Session
from datetime import datetime,timedelta,timezone
load_dotenv()
key=os.getenv("key")
kieu=os.getenv("kieu")
minOs=int(os.getenv("min"))
def create_token(user_id:str, role:str,db:Session): 
    ex=datetime.now(timezone.utc)+timedelta(minutes=minOs)
    paload={
         "sub": str(user_id), 
         "role":role,
         "exp":ex
    }
    return jwt.encode( 
         paload,
        kieu, 
        algorithm=int(key)
    )
def token_decode(token:str): 
    return jwt.decode( 
         token, 
         kieu, 
        algorithms=int(key)
    )