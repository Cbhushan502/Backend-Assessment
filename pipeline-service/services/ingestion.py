import requests
import dlt

FLASK_URL = "http://mock-server:5000/api/customers"

def fetch_all_customers():
    all_customers = []
    page = 1
    limit = 10

    while True:
        res = requests.get(FLASK_URL, params={"page": page, "limit": limit})
        res.raise_for_status()
        data = res.json()

        customers = data["data"]
        if not customers:
            break

        all_customers.extend(customers)

        if len(customers) < limit:
            break

        page += 1

    return all_customers


def load_to_postgres(customers):
    pipeline = dlt.pipeline(
        pipeline_name="customer_pipeline",
        destination="postgres",
        dataset_name="public"   # 👈 IMPORTANT: use default schema
    )

    load_info = pipeline.run(
        customers,
        table_name="customers",  # 👈 FORCE table name
        write_disposition="replace"  # for testing
    )

    return load_info
