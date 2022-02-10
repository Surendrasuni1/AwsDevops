import boto3

client = boto3.client('ec2',region_name='us-west-2',aws_access_key_id='aaaaaaaaaaaaaaaaaaaaaa',aws_secret_access_key='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
response =client.describe_instances()
print(response)
for data in response['ResponseMetadata']:
	print(data)





	
