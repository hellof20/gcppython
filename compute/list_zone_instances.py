import googleapiclient.discovery
from google.oauth2 import service_account

project = 'ultra-compound-305409'
zone = 'us-central1-a'
credentials = service_account.Credentials.from_service_account_file('ultra-compound-305409-1b14cec22512.json')
compute = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)  # create compute engine service
result = compute.instances().list(project=project, zone=zone).execute()  # get one zone instances
#result = compute.instances().aggregatedList(project=project).execute()    # get all instances
print(result)