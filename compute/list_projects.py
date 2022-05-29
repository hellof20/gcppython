import googleapiclient.discoveryi as discovery
from google.oauth2 import service_account

#credentials = service_account.Credentials.from_service_account_file('ultra-compound-305409-1b14cec22512.json')
compute = discovery.build('compute', 'v1')  # create compute engine service
resourcemanager = discovery.build('cloudresourcemanager', 'v1')

result = resourcemanager.projects().list().execute()
for dict in result['projects']:
    print(dict['projectId'])

regions = compute.regions().list(project=projectId).execute()
for region in regions['items']:
    print(region['name'])

# result = compute.instances().list(project=project, zone=zone).execute()
