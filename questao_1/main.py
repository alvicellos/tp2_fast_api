from fastapi import FastAPI
from routes import router

'''
uvicorn main:app --reload
    ->      http://127.0.0.1:8000/docs  (a documentação interativa)
'''

app = FastAPI()
app.include_router(router)