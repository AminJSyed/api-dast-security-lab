from fastapi import FastAPI, Header, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="API DAST Security Lab",
    description="API security lab for OWASP ZAP DAST scanning",
    version="1.0.0"
)


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
        "owner_id": "amin",
        "route": "Frankfurt to Berlin",
        "status": "CONFIRMED"
    },
    "1002": {
        "booking_id": "1002",
        "customer": "Test User",
        "owner_id": "test-user",
        "route": "Munich to Hamburg",
        "status": "PENDING"
    }
}


TOKENS = {
    "token-amin": "amin",
    "token-test": "test-user"
}


def public_booking(booking: dict):
    return {
        "booking_id": booking["booking_id"],
        "customer": booking["customer"],
        "route": booking["route"],
        "status": booking["status"]
    }


class LoginRequest(BaseModel):
    username: str
    password: str


def get_current_user(authorization: str | None):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization scheme"
        )

    token = authorization.replace("Bearer ", "")
    user_id = TOKENS.get(token)

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return user_id


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
def search(query: str = Query(...)):
    return {
        "query": query,
        "result": f"You searched for: {query}"
    }


@app.get("/booking/{booking_id}")
def get_booking(
    booking_id: str,
    authorization: str | None = Header(default=None)
):
    current_user = get_current_user(authorization)

    booking = BOOKINGS.get(booking_id)

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    if booking["owner_id"] != current_user:
        raise HTTPException(
            status_code=403,
            detail="Access denied for this booking"
        )

    return public_booking(booking)


@app.post("/login")
def login(payload: LoginRequest):
    if payload.username == "amin" and payload.password == "amin123":
        return {
            "access_token": "token-amin",
            "token_type": "bearer"
        }

    if payload.username == "test" and payload.password == "test123":
        return {
            "access_token": "token-test",
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )


@app.get("/debug")
def debug():
    return {
        "debug": False,
        "message": "Debug output is disabled in this lab."
    }
