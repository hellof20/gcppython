from google.cloud import monitoring_v3
import tabulate

def list_uptime_check_ips():
    client = monitoring_v3.UptimeCheckServiceClient()
    ips = client.list_uptime_check_ips(request={})
    print(
        tabulate.tabulate(
            [(ip.region, ip.location, ip.ip_address) for ip in ips],
            ("region", "location", "ip_address"),
        )
    )
list_uptime_check_ips()
