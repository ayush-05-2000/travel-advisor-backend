from fastapi import FastAPI
from app.routes import user_routes, place_routes, itinerary_routes, feedback_routes, expense_routes,auth_routes, download_routes, destination_routes, collaborator_routes
import webbrowser
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="T Guide API", version="1.0")

# Registering the routes
app.include_router(collaborator_routes.router)
app.include_router(destination_routes.router)
app.include_router(download_routes.router)
app.include_router(expense_routes.router)
app.include_router(feedback_routes.router)
app.include_router(itinerary_routes.router)
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
app.include_router(place_routes.router)



# # Define the OAuth2 token-based authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# @app.get("/secured-endpoint")
# def secured_endpoint(token: str = Depends(oauth2_scheme)):
#     return {"message": "This is a secured endpoint"}

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from frontend
    allow_credentials=True,  # Allow cookies and authorization headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Advisor API"}

if __name__ == "__main__":
    import uvicorn
    print("API documentation available at: http://127.0.0.1:8000/docs")
    webbrowser.open("http://127.0.0.1:8000/docs")  # Automatically open browser
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
 
