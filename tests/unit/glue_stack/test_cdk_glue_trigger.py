"""Unit test for glue triggers created by cdk_glue_stack.py"""
import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_datapipeline.cdk_glue_stack import CdkGlueStack


def test_glue_trigger_created():
    """Test if the resources is created with correct configuration"""
    app = core.App()
    stack = CdkGlueStack(app, "cdk-glue")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Glue::Trigger",
        {
            "Actions": [
                {
                    "JobName": "GlueJob1",
                    "NotificationProperty": {"NotifyDelayAfter": 2},
                    "Timeout": 2,
                }
            ],
            "Type": "SCHEDULED",
            "Name": "GlueTrigger1",
            "Schedule": "cron(0 0 * * ? *)",
            "StartOnCreation": False,
        },
    )

    template.has_resource_properties(
        "AWS::Glue::Trigger",
        {
            "Actions": [
                {
                    "JobName": "GlueJob2",
                    "NotificationProperty": {"NotifyDelayAfter": 2},
                    "Timeout": 2,
                }
            ],
            "Type": "CONDITIONAL",
            "Name": "GlueTrigger2",
            "Predicate": {
                "Conditions": [
                    {
                        "JobName": "GlueJob1",
                        "LogicalOperator": "EQUALS",
                        "State": "SUCCEEDED",
                    }
                ]
            },
            "StartOnCreation": False,
        },
    )


def test_glue_trigger_resource_count():
    """Test if the number of resources is created accurately"""
    app = core.App()
    stack = CdkGlueStack(app, "cdk-glue")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Glue::Trigger", 2)
