
import boto3

ec2_client_sydney = boto3.client('ec2', region_name="ap-southeast-2")
ec2_resource_sydney = boto3.resource('ec2', region_name="ap-southeast-2")


instance_ids_sydney = []


reservations_paris = ec2_client_sydney.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instance_ids_sydney.append(ins['InstanceId'])


response = ec2_resource_sydney.create_tags(
    Resources=instance_ids_sydney,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


ec2_client_melbourne = boto3.client('ec2', region_name="eu-central-1")
ec2_resource_melbourne = boto3.resource('ec2', region_name="eu-central-1")

instance_ids_melbourne = []

reservations_melbourne = ec2_client_melbourne.describe_instances()['Reservations']
for res in reservations_melbourne:
    instances = res['Instances']
    for ins in instances:
        instance_ids_melbourne.append(ins['InstanceId'])


response = ec2_resource_melbourne.create_tags(
    Resources=instance_ids_melbourne,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)