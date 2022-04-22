from google.cloud import monitoring_v3
import time

client = monitoring_v3.MetricServiceClient()
project_name = "projects/speedy-victory-336109"
now = time.time()
seconds = int(now)
nanos = int((now - seconds) * 10 ** 9)
interval = monitoring_v3.TimeInterval(
    {
        "end_time": {"seconds": seconds, "nanos": nanos},
        "start_time": {"seconds": (seconds - 1200), "nanos": nanos},
    }
)
results = client.list_time_series(
    request={
        "name": project_name,
        "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
        "interval": interval,
        "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.HEADERS,
    }
)
for result in results:
    print(result)
