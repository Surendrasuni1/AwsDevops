import boto3

client =boto3.client('ec2',region_name='us-west-2',aws_access_key_id='pppppppppppppppY',aws_secret_access_key='oooooooooooooooooooooooooooooo')

#igw_detach_response=client.detach_internet_gateway(InternetGatewayId='igw-0c7aa6c14d8d5c7d5',VpcId='vpc-04ba23e9278acfcd0')
#print(igw_detach_response)
print('igw detached successfully')
#route_delete_response = client.delete_route(
#    DestinationCidrBlock='0.0.0.0/0',   
#   RouteTableId='rtb-0dfd3cde3092122e9'
#)
#print(route_delete_response)
print('route deleted successfully')

#disassociate_routetable_response01=client.disassociate_route_table(AssociationId='rtbassoc-0763a4665055585a5')
print("disassociated rtbassoc-0763a4665055585a5  successfully ")
#disassociate_routetable_response01=client.disassociate_route_table(AssociationId='rtbassoc-05e367c5412ab068b')
print("disassociated rtbassoc-05e367c5412ab068b  successfully ")



#igw_delete_response=client.delete_internet_gateway(InternetGatewayId='igw-0c7aa6c14d8d5c7d5')
#print(igw_delete_response)
print('igw delete successfully')

routetable_delete_response=client.delete_route_table(RouteTableId='rtb-0dfd3cde3092122e9')
print(routetable_delete_response)
print('routetable deleted successfully')

subnet01_delete_response=client.delete_subnet(SubnetId='subnet-0254d44604a2cd4eb')
print(subnet01_delete_response)
print('subnet deleted successfully')


subnet02_delete_response=client.delete_subnet(SubnetId='subnet-02c25114066e9390c')
print(subnet02_delete_response)
print('subnet deleted successfully')

vpc_delete_response=client.delete_vpc(VpcId='vpc-04ba23e9278acfcd0')
print(vpc_delete_response)
print('vpc delted successfully')
