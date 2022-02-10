import boto3

client =boto3.client('s3',aws_access_key_id='aaaaaaaaaaaaaaa',aws_secret_access_key='bbbbbbbbbbbbbbbbbbbbbbb')
response=client.list_buckets()
print(response['ResponseMetadata'])
#
	#
