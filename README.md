# Backend Assessment – Dockerized Microservices

This project demonstrates a production-style backend system using microservices, Docker, FastAPI, Flask, and PostgreSQL.  
It includes a mock data service, an ingestion pipeline, and persistent storage with a clean API design.

---

## 🧩 Architecture Overview

The system consists of three services:

1. **Mock Server (Flask)**
   - Serves static customer data
   - Port: `5000`

2. **Pipeline Service (FastAPI)**
   - Fetches data from mock server
   - Stores it into PostgreSQL
   - Exposes REST APIs
   - Port: `8000`

3. **PostgreSQL**
   - Persistent storage
   - Port: `5432`

All services are containerized using Docker Compose.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Flask
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy
- Pydantic

---

## 🚀 How to Run

### Prerequisites
- Docker
- Docker Compose

### Start all services
```bash
docker compose up --build
