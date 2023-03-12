"""Unit test for glue jobs created by cdk_glue_stack.py"""
import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_datapipeline.cdk_glue_stack import CdkGlueStack


def test_glue_job_created():
    """Test if the resources is created with correct configuration"""
    app = core.App()
    stack = CdkGlueStack(app, "cdk-glue")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Glue::Job",
        {
            "Command": {
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script",
            },
            "Role": "your_glue_role_arn",
            "DefaultArguments": {
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp1",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties",
            },
            "ExecutionProperty": {"MaxConcurrentRuns": 1},
            "GlueVersion": "2.0",
            "MaxRetries": 2,
            "Name": "GlueJob1",
            "NumberOfWorkers": 2,
            "Timeout": 2,
            "WorkerType": "G.1X",
        },
    )

    template.has_resource_properties(
        "AWS::Glue::Job",
        {
            "Command": {
                "Name": "glueetl",
                "ScriptLocation": "s3://testing-script-1234/glue-script/testing-glue-script",
            },
            "Role": "your_glue_role_arn",
            "DefaultArguments": {
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp2",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties",
            },
            "ExecutionProperty": {"MaxConcurrentRuns": 1},
            "GlueVersion": "2.0",
            "MaxRetries": 2,
            "Name": "GlueJob2",
            "NumberOfWorkers": 2,
            "Timeout": 2,
            "WorkerType": "G.1X",
        },
    )


def test_glue_job_resource_count():
    """Test if the number of resources is created accurately"""
    app = core.App()
    stack = CdkGlueStack(app, "cdk-glue")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Glue::Job", 2)
