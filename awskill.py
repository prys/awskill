#! /usr/local/bin/python3
import boto3
ec2top = boto3.client('ec2')
response = ec2top.describe_regions()

for regionDetails in response['Regions']:
    print('Looking in region ' + regionDetails['RegionName'])
    ec2 = boto3.client('ec2', regionDetails['RegionName'])
    ec2Response = ec2.describe_instances()
    for i in range (len(ec2Response['Reservations'])):
        thisInstance = ec2Response['Reservations'][i]['Instances'][0]['InstanceId']
        thisState = ec2Response['Reservations'][i]['Instances'][0]['State']['Name']
        termProt = ec2.describe_instance_attribute(Attribute='disableApiTermination', InstanceId=thisInstance)
        print('Found instance ' + thisInstance)
        if termProt and (thisState != 'terminated'):
            modResponse = ec2.modify_instance_attribute(Attribute='disableApiTermination', Value='False', InstanceId=thisInstance)
            termResponse = ec2.terminate_instances(InstanceIds=[thisInstance])
