from aws_cdk import (
    Stack,
    aws_glue as glue,
)
from constructs import Construct

class CdkGlueStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create a Glue Trigger
        trigger1 = glue.CfnTrigger(
            self, "GlueTrigger1",
            type='SCHEDULED',
            schedule='cron(0 0 * * ? *)',
            actions=[{
                'JobName': 'GlueJob1'
            }]
        )

        # Create a Glue Job
        job1 = glue.CfnJob(
            self, "GlueJob1",
            command={
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script"
            },
            default_arguments={
                "--JOB_NAME": "Job1",
                "--tempdir": "s3://testing-script-1234/glue-temp/temp1"
            },
            role="your_glue_role_arn",
        )

        # Create a Glue Trigger
        trigger2 = glue.CfnTrigger(
            self, "GlueTrigger2",
            type='CONDITIONAL',
            actions=[{
                'JobName': 'GlueJob2'
            }],
            predicate={
                'Conditions': [{
                    'JobName': 'GlueJob1',
                    'State': 'SUCCEEDED'
                }]
            }
        )

        # Create a Glue Job
        job2 = glue.CfnJob(
            self, "GlueJob2",
            command={
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script"
            },
            default_arguments={
                "--JOB_NAME": "Job2",
                "--tempdir": "s3://testing-script-1234/glue-temp/temp2"
            },
            role="your_glue_role_arn",
        )

        # Create a Glue Trigger
        trigger3 = glue.CfnTrigger(
            self, "GlueTrigger3",
            type='CONDITIONAL',
            actions=[{
                'CrawlerName': 'GlueCrawler'
            }],
            predicate={
                'Conditions': [{
                    'JobName': 'GlueJob2',
                    'State': 'SUCCEEDED'
                }]
            }
        )
