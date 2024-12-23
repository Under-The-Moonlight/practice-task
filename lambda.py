import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    test_list =[]
    bucket = s3.Bucket('my-test-bucket-dkostin')
    for obj in bucket.objects.all():
        print(obj.key)
        test_list.append(obj.key)

    
    return obj.key
