from fastapi import FastAPI
from routes.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
