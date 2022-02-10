import boto3

client =boto3.client('s3',aws_access_key_id='AKIAQA3SUJXDWHSDUUVY',aws_secret_access_key='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')
response=client.list_buckets()
print(response['ResponseMetadata'])
#
	#