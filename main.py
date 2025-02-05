from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )

@app.get("/")
def read_root():
    ISO = datetime.now().isoformat() + 'Z'
    return {
            "email": "abdulsemiukusimo@gmail.com",
            "current_datetime": ISO,
            "github_url": "https://github.com/Kusimo4real/HNG-Internship"
            }
