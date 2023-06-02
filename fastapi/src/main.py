# isort: skip_file
# ^ This is performed to ensure the imports are not removed even though they are not utilized
import uvicorn


from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
router = APIRouter()


app.include_router(router)


@app.get("/health", status_code=200)
@app.get("/api/health", status_code=200)
async def home():
    return {"status": "up"}


if __name__ == "__main__":
    # Because the Celery workers are started on the same VM they share the same CPU IO as the main app.
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)
