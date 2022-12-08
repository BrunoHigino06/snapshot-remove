import boto3, json, datetime


def scan_snapshots():
    day = 8
    month = 12
    year = 2022
    delta = 30
    date_refence = datetime.datetime(year, month, day).strftime('%Y-%m-%d')
    
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
    for snapshots in response_iterator:
        while 
        for snapshot in snapshots["Snapshots"]:
            date = datetime.datetime.date(snapshot["StartTime"])
            datestr = date.strftime('%Y-%m-%d')
            if datestr == date_refence:
                print(datestr)

scan_snapshots()
