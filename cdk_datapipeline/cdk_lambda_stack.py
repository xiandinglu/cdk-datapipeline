from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_s3 as s3,
)
from constructs import Construct

class CdkLambdaStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # # create an S3 bucket to store the Lambda function code
        # bucket = s3.Bucket(self, 'MyBucket', bucket_name='cdk-lambda-script')

        my_function = lambda_.Function(
            self, 'MyFunction',
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler='index.handler',
            code=lambda_.Code.from_asset('./lambda'),
            function_name='FunctionCreatedByCDK'
            # layers=[layer]
        )