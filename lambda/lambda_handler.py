import json

def lambda_handler(event, context):
    ## Logic
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }