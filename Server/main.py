from fastapi import FastAPI
from Connection.connection import Base,eng
Base.metadata.create_all(bind=eng)
app=FastAPI()
@app.get("/tan")
def tan(): 
    return "server da tra ve thanh cong"