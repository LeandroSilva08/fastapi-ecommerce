from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce User Service",
    version="0.1.0",
    description="Microservice responsible for user management.",
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "users"}
