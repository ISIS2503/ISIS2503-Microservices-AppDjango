import uvicorn
from fastapi import FastAPI
import views

def create_app():
    app = FastAPI(
        docs_url="/places/docs",
        redoc_url=None,
    )
    
    app.include_router(views.router)

    return app

if __name__ == "__main__":
    app = create_app()
    # avoid redirects
    uvicorn.run(app, host="0.0.0.0", port=8000)