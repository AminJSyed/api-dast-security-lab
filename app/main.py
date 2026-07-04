from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="API DAST Security Lab",
    description="API security lab for OWASP ZAP DAST scanning",
    version="1.0.0"
)

# Intentionally permissive CORS for DAST learning
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    return response


BOOKINGS = {
    "1001": {
        "booking_id": "1001",
        "customer": "Amin",
        "route": "Frankfurt to Berlin",
        "status": "CONFIRMED"
    },
    "1002": {
        "booking_id": "1002",
        "customer": "Test User",
        "route": "Munich to Hamburg",
        "status": "PENDING"
    }
}


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def root():
    return {
        "message": "API DAST Security Lab",
        "docs": "/docs",
        "openapi": "/openapi.json"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/search")
def search(query: str = Query(..., description="Search route or booking")):
    return {
        "query": query,
        "result": f"You searched for: {query}"
    }


@app.get("/booking/{booking_id}")
def get_booking(booking_id: str):
    booking = BOOKINGS.get(booking_id)

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


@app.post("/login")
def login(payload: LoginRequest):
    if payload.username == "admin" and payload.password == "admin123":
        return {
            "access_token": "demo-insecure-token",
            "token_type": "bearer"
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/debug")
def debug():
    return {
        "debug": False,
        "message": "Debug output is disabled in this lab."
    }
