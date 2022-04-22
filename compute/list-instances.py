import typing

import google.cloud.compute_v1 as compute_v1

def list_instances(project_id: str, zone: str) -> typing.Iterable[compute_v1.Instance]:
    instance_client = compute_v1.InstancesClient()
    instance_list = instance_client.list(project=project_id, zone=zone)

    print(f"Instances found in zone {zone}:")
    for instance in instance_list:
        print(f" - {instance.name} ({instance.machine_type})")

    return instance_list

print(list_instances('speedy-victory-336109'))
