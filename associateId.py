import  boto3

client =boto3.client('ec2',region_name='us-west-2',aws_access_key_id='aaaaaaaaaaaaaa',aws_secret_access_key='bbbbbbbbbbbbbb')

response=  client.describe_route_tables(
    RouteTableIds=[
        'rtb-095a96a6be53703e8',
    ],
)
#print(response['RouteTables'])
for i in response['RouteTables']:
	for j in i['Associations']:
		print (j['RouteTableAssociationId'])

