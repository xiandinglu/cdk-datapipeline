import aws_cdk as core
import aws_cdk.assertions as assertions

# from cdk_datapipeline.cdk_datapipeline_stack import CdkDatapipelineStack
from cdk_datapipeline.cdk_glue_stack import CdkGlueStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_datapipeline/cdk_datapipeline_stack.py
def test_glue_pipeline_created():
    app = core.App()
    stack = CdkGlueStack(app, "cdk-glue")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Glue::Job",
        {
            "Command": {
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script"
            },
            "Role": "your_glue_role_arn",
            'DefaultArguments': {
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp1",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties"
            },
            "ExecutionProperty": {
                "MaxConcurrentRuns": 1
            },
            "GlueVersion": "2.0",
            "MaxRetries": 2,
            "Name": "GlueJob1",
            "NumberOfWorkers": 2,
            "Timeout": 2,
            "WorkerType": "G.1X"
        }
    )

    template.has_resource_properties(
        "AWS::Glue::Job",
        {
            "Command": {
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script"
            },
            "Role": "your_glue_role_arn",
            'DefaultArguments': {
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp2",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties"
            },
            "ExecutionProperty": {
                "MaxConcurrentRuns": 1
            },
            "GlueVersion": "2.0",
            "MaxRetries": 2,
            "Name": "GlueJob2",
            "NumberOfWorkers": 2,
            "Timeout": 2,
            "WorkerType": "G.1X"
        }
    )

    template.resource_count_is("AWS::Glue::Job", 2)

    template.has_resource_properties(
        "AWS::Glue::Trigger",
        {
            "Actions": [
                {
                    "JobName": "GlueJob1",
                    "NotificationProperty": {
                        "NotifyDelayAfter": 2
                    },
                    "Timeout": 2
                }
            ],
            "Type": "SCHEDULED",
            "Name": "GlueTrigger1",
            "Schedule": "cron(0 0 * * ? *)",
            "StartOnCreation": False
        }
    )

    template.has_resource_properties(
        "AWS::Glue::Trigger",
        {
            "Actions": [
                {
                    "JobName": "GlueJob2",
                    "NotificationProperty": {
                        "NotifyDelayAfter": 2
                    },
                    "Timeout": 2
                }
            ],
            "Type": "CONDITIONAL",
            "Name": "GlueTrigger2",
            "Predicate": {
                "Conditions": [
                    {
                        "JobName": "GlueJob1",
                        "LogicalOperator":"EQUALS",
                        "State": "SUCCEEDED"
                    }
                ]
            },
            "StartOnCreation": False
        }
    )
    template.resource_count_is("AWS::Glue::Trigger", 2)
