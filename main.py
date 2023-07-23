import psutil
import requests
import matplotlib.pyplot as plt
import sqlite3
import datetime as dt
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

class Solaris(BaseModel):
    keyinput: str


app = FastAPI()

@app.get("/")
def root():
    html_content = "hello, world"
    return HTMLResponse(content=html_content)

@app.post("/")
def input(keyinput: Solaris):
    return keyinput




#con = sqlite3.connect('data.db')
#cur = con.cursor()
#cur.execute("CREATE TABLE info (Time, CPU, GPU)")


#while True:
#    cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
#    time = dt.datetime.now().strftime('%H:%M:%S')
#    ram_usage = psutil.virtual_memory()
#$    print(f' Занятость процессора: {cpu_usage}%, Занятость оперативной памяти: {ram_usage[2]}%')
#    entity = (time, cpu_usage, ram_usage[2])
#    cur.execute("INSERT INTO info (Time, CPU, GPU) VALUES(?, ?, ?)", entity)
#    con.commit()



