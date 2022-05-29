import googleapiclient.discovery as discovery
from google.cloud import monitoring_v3
from google.cloud import redis_v1
import time

projects=["speedy-victory-336109"]

metric = monitoring_v3.MetricServiceClient()
sqladmin = discovery.build('sqladmin', 'v1beta4')
redis = redis_v1.CloudRedisClient()

def list_projects():
    resourcemanager = discovery.build('cloudresourcemanager', 'v1')
    result = resourcemanager.projects().list().execute()
    for dict in result['projects']:
        print(dict['projectId'])

def check_sql_maintenance(project):
    req = sqladmin.instances().list(project=project)
    resp = req.execute()
    maintain_instances = []
    for key, value in resp.items():
        for dict in value:
            if 'scheduledMaintenance' in dict:
                maintain_instances.append(dict['name'])
    return maintain_instances

def check_redis_maintenance(project, region):
    req = redis_v1.ListInstancesRequest(parent="projects/%s/locations/%s" %(project,region))
    maintain_instances = []
    page_result = redis.list_instances(request=req)
    for response in page_result:
        print(response)

def write_metric(project, instance, value):
    project = "projects/"+project
    series = monitoring_v3.TimeSeries()
    # series.metric.type = "custom.googleapis.com/my_metric" + str(uuid.uuid4())
    series.metric.type = "custom.googleapis.com/CloudSQL_Maintance"
    series.metric.labels["sql_instance"] = instance
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": value}})
    series.points = [point]
    metric.create_time_series(name=project, time_series=[series])

for project in projects:
    # sql_instances = check_sql_maintenance(project)
    sql_instances = ['mysql']
    if len(sql_instances) > 0:
        for sql_instance in sql_instances:
            write_metric(project, sql_instance, 1.0)
            print(project + ': writed maintaince data to metric')    
    else:
        print(project + ': no maintaince')
