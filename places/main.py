import uvicorn
from fastapi import FastAPI
import views

def create_app():
    app = FastAPI()
    
    app.include_router(views.router, prefix=views.API_PREFIX)

    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)