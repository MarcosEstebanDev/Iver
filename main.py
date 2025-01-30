from fastapi import FastAPI
from bot.gui_bot import open_notepad_and_write

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI está corriendo correctamente"}

@app.get("/run-bot")
def run_bot():
    result = open_notepad_and_write()
    return {"status": "success", "message": result}
