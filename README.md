# Observability with FastAPI + Prometheus + Grafana

Demonstration project for the article "Observability in Modern Applications: Prometheus + Grafana + Python" published on Medium.  
Implements observability practices applied to an order management API.

## Requirements

- Python 3.11 or higher
- Docker and Docker Compose

## Install

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest tests/ -v
```

## Run the full stack

```bash
docker-compose up --build
```

Services available at:

- API → http://localhost:8000
- Prometheus → http://localhost:9090
- Grafana → http://localhost:3000 (user: `admin`, password: `admin`)

## Project Structure

```
├── app/
│   ├── main.py           # FastAPI app with metrics
│   └── metrics.py        # Prometheus metrics definition
├── tests/
│   └── test_main.py      # API tests
├── prometheus/
│   └── prometheus.yml    # Prometheus config
├── docker-compose.yml    # Full observability stack
├── Dockerfile            # API image
└── .github/workflows/    # CI/CD pipeline
```

## Article

[Observability in Modern Applications: Prometheus + Grafana + Python](https://medium.com/@jm2022075474/observability-in-modern-applications-prometheus-grafana-python-499e11e94e12?sharedUserId=jm2022075474)

## Student

Junior Mamani Estaña