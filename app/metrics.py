from prometheus_client import Counter, Histogram, REGISTRY

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds",
    "API request duration in seconds",
    ["endpoint"]
)

ERROR_COUNT = Counter(
    "api_errors_total",
    "Total number of API errors",
    ["endpoint"]
)