#! /usr/local/bin/python3
import boto3
ec2top = boto3.client('ec2')
response = ec2top.describe_regions()

for regionDetails in response['Regions']:
    print('Looking in region ' + regionDetails['RegionName'])
    ec2 = boto3.client('ec2', regionDetails['RegionName'])
    ec2Response = ec2.describe_instances()
    for ins in ec2Response['Reservations']:
        thisInstance = ins['Instances'][0]['InstanceId']
        thisState = ins['Instances'][0]['State']['Name']
        termProt = ec2.describe_instance_attribute(Attribute='disableApiTermination', InstanceId=thisInstance)
        print('Found instance ' + thisInstance + '    State = ' + thisState)
        if termProt and (thisState != 'terminated'):
            modResponse = ec2.modify_instance_attribute(Attribute='disableApiTermination', Value='False', InstanceId=thisInstance)
        termResponse = ec2.terminate_instances(InstanceIds=[thisInstance])
    natResponse = ec2.describe_nat_gateways()
    for natGWs in natResponse['NatGateways']:
        print('Found NAT G/W: ' + natGWs['NatGatewayId'] + '   State = ' + natGWs['State'])
        if natGWs['State'] != 'deleted':
            gwDel = ec2.delete_nat_gateway(NatGatewayId=natGWs['NatGatewayId'])
    elasticResponse = ec2.describe_addresses()
    for elIPs in elasticResponse['Addresses']:
        print('Found Elastic IP: ' + elIPs['AllocationId'])
        ipDel = ec2.release_address(AllocationId=elIPs['AllocationId'])
