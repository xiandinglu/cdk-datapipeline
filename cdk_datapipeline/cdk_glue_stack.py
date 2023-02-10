from aws_cdk import (
    Stack,
    aws_glue as glue,
)
from constructs import Construct

class CdkGlueStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create a Glue Job
        job1 = glue.CfnJob(
            self, "GlueJob1",
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                script_location="s3://testing-script-1234/glue-script/testing-glue-script"
            ),
            role="your_glue_role_arn",

            # the properties below are optional
            # allocated_capacity=123,
            # connections=glue.CfnJob.ConnectionsListProperty(
            #     connections=["connections"]
            # ),
            default_arguments={
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp1",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties"
            },
            # description="description",
            # execution_class="executionClass",
            execution_property=glue.CfnJob.ExecutionPropertyProperty(
                max_concurrent_runs=1
            ),
            glue_version="2.0",
            max_retries=2,
            name="GlueJob1",
            # non_overridable_arguments=non_overridable_arguments,
            # notification_property=glue.CfnJob.NotificationPropertyProperty(
            #     notify_delay_after=123
            # ),
            number_of_workers=2,
            timeout=2,
            worker_type="G.1X"
        )

        # Create second Glue Job
        job2 = glue.CfnJob(
            self, "GlueJob2",
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                script_location="s3://testing-script-1234/glue-script/testing-glue-script"
            ),
            role="your_glue_role_arn",

            # the properties below are optional
            # allocated_capacity=123,
            # connections=glue.CfnJob.ConnectionsListProperty(
            #     connections=["connections"]
            # ),
            default_arguments={
                "--job-language": "python",
                "--job-name": "Job1",
                "--TempDir": "s3://testing-script-1234/glue-temp/temp2",
                "--job-bookmark-option": "job-bookmark-disable",
                "--extra-files": "s3://testing-script-1234/log4j-properties-config/log4j.properties"
            },
            # description="description",
            # execution_class="executionClass",
            execution_property=glue.CfnJob.ExecutionPropertyProperty(
                max_concurrent_runs=1
            ),
            glue_version="2.0",
            max_retries=2,
            name="GlueJob2",
            # non_overridable_arguments=non_overridable_arguments,
            # notification_property=glue.CfnJob.NotificationPropertyProperty(
            #     notify_delay_after=123
            # ),
            number_of_workers=2,
            timeout=2,
            worker_type="G.1X"
        )

        # Create a Glue Trigger
        trigger1 = glue.CfnTrigger(
            self, "GlueTrigger1",
            actions=[glue.CfnTrigger.ActionProperty(
                job_name="GlueJob1",
                notification_property=glue.CfnTrigger.NotificationPropertyProperty(
                    notify_delay_after=2
                ),
                timeout=2
            )],
            type="SCHEDULED",
            name="GlueTrigger1",
            schedule="cron(0 0 * * ? *)",
            start_on_creation=False,
        )

        # Create second Glue Trigger
        trigger2 = glue.CfnTrigger(
            self, "GlueTrigger2",
            actions=[glue.CfnTrigger.ActionProperty(
                job_name="GlueJob2",
                notification_property=glue.CfnTrigger.NotificationPropertyProperty(
                    notify_delay_after=2
                ),
                timeout=2
            )],
            type="CONDITIONAL",
            name="GlueTrigger2",
            predicate=glue.CfnTrigger.PredicateProperty(
                conditions=[glue.CfnTrigger.ConditionProperty(
                    job_name="GlueJob1",
                    logical_operator="EQUALS",
                    state="SUCCEEDED"
                )],
            ),
            start_on_creation=False,
        )
