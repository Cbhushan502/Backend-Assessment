from fastapi import FastAPI, HTTPException, Query
from database import SessionLocal, engine
from models.customer import Customer, Base
from services.ingestion import fetch_all_customers, load_to_postgres

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/ingest")
def ingest():
    try:
        customers = fetch_all_customers()
        load_to_postgres(customers)
        return {"status": "success", "records_processed": len(customers)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/customers")
def get_customers(page: int = Query(1), limit: int = Query(10)):
    db = SessionLocal()
    offset = (page - 1) * limit
    customers = db.query(Customer).offset(offset).limit(limit).all()
    total = db.query(Customer).count()

    data = []
    for c in customers:
        data.append({
            "customer_id": c.customer_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "phone": c.phone,
            "address": c.address,
            "date_of_birth": str(c.date_of_birth),
            "account_balance": float(c.account_balance),
            "created_at": str(c.created_at)
        })

    return {
        "data": data,
        "total": total,
        "page": page,
        "limit": limit
    }

@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str):
    db = SessionLocal()
    c = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    if not c:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {
        "customer_id": c.customer_id,
        "first_name": c.first_name,
        "last_name": c.last_name,
        "email": c.email,
        "phone": c.phone,
        "address": c.address,
        "date_of_birth": str(c.date_of_birth),
        "account_balance": float(c.account_balance),
        "created_at": str(c.created_at)
    }
