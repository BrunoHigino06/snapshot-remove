import boto3
import json

def scan_snapshots():
    date = "01/01/0001"
    client = boto3.client('ec2', region_name='us-east-1')
    paginator = client.get_paginator('describe_snapshots')

    response_iterator = paginator.paginate(
        OwnerIds=[
        'self',
        ],
        PaginationConfig={
            'PageSize':100,
        }
    )
    for i in response_iterator:
        print (json.dumps(i, indent=4, default=str))
        

scan_snapshots()
