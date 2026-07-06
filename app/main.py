import time
import random
from fastapi import FastAPI, HTTPException
from prometheus_client import make_asgi_app
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT

app = FastAPI(title="Orders API")

# Exponer métricas en /metrics para que Prometheus haga scraping
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/orders")
def get_orders():
    start = time.time()
    try:
        # Simulamos latencia variable
        time.sleep(random.uniform(0.01, 0.3))
        REQUEST_COUNT.labels(method="GET", endpoint="/orders", status="200").inc()
        return {"orders": ["order_1", "order_2", "order_3"]}
    except Exception:
        ERROR_COUNT.labels(endpoint="/orders").inc()
        REQUEST_COUNT.labels(method="GET", endpoint="/orders", status="500").inc()
        raise HTTPException(status_code=500, detail="Internal error")
    finally:
        REQUEST_LATENCY.labels(endpoint="/orders").observe(time.time() - start)


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    start = time.time()
    try:
        time.sleep(random.uniform(0.01, 0.15))
        # Simulamos un 20% de errores
        if random.random() < 0.2:
            ERROR_COUNT.labels(endpoint="/orders/{order_id}").inc()
            REQUEST_COUNT.labels(
                method="GET", endpoint="/orders/{order_id}", status="404"
            ).inc()
            raise HTTPException(status_code=404, detail="Order not found")

        REQUEST_COUNT.labels(
            method="GET", endpoint="/orders/{order_id}", status="200"
        ).inc()
        return {"order_id": order_id, "status": "shipped"}
    finally:
        REQUEST_LATENCY.labels(endpoint="/orders/{order_id}").observe(time.time() - start)


@app.get("/health")
def health():
    return {"status": "ok"}