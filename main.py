from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.route import router
app = FastAPI()

app.include_router(router)
