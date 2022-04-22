import googleapiclient.discovery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('ultra-compound-305409-1b14cec22512.json')
compute = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)  # create compute engine service
resourcemanager = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=credentials)  # create compute engine service

result = resourcemanager.projects().list().execute()
projectId = result['projects'][0]['projectId']
regions = compute.regions().list(project=projectId).execute()
for region in regions['items']:
    print(region['name'])
# result = compute.instances().list(project=project, zone=zone).execute()
