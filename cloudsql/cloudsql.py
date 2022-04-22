import argparse
import os
import time
import json

import googleapiclient.discovery as discovery

service = discovery.build('sqladmin', 'v1beta4')

req = service.instances().list(project="my-project-2-337005")
resp = req.execute()
print(json.dumps(resp, indent=2))
