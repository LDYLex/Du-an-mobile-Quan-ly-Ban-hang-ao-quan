from fastapi import FastAPI
from Connection.connection import Base 
Base.metadata.create_all()
app=FastAPI()
