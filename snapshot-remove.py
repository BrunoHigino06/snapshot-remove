import boto3, json, datetime, os


def scan_snapshots():
    start_day = 15
    start_month = 12
    start_year = 2022
    delta = 365
    from_date = 0


    reference_date = datetime.datetime(start_year, start_month, start_day)
    
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
        while delta >= 0:
            start_date = reference_date - datetime.timedelta(days=(from_date))
            delta = delta -1
            final_date = start_date - datetime.timedelta(days=(delta))
            formated_final_date = final_date.strftime('%Y-%m-%d')
            for snapshot in snapshots["Snapshots"]:
                date = datetime.datetime.date(snapshot["StartTime"])
                snapshot_date = date.strftime('%Y-%m-%d')
                if snapshot_date == formated_final_date:
                    snapshotid = snapshot["SnapshotId"]
                    print("Removing snapshot from: "+formated_final_date+" whith ID: "+snapshotid)
                    os.system('aws ec2 delete-snapshot --snapshot-id '+snapshotid)


                    




scan_snapshots()
