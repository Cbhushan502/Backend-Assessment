# Backend Assessment – Dockerized Microservices

## Services
- Mock Server (Flask) → Port 5000
- Pipeline Service (FastAPI) → Port 8000
- PostgreSQL → Port 5432

## Run Project

docker compose up --build

## Test

Mock Server:
http://localhost:5000/customers

Pipeline Service:
http://localhost:8000/fetch-customers

---

This will:
✔ Fetch customers  
✔ Store them in PostgreSQL  
✔ Return inserted records  
✔ Fully Dockerized  
✔ Mac compatible  
