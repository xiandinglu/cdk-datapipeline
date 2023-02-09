import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_datapipeline.cdk_datapipeline_stack import CdkDatapipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_datapipeline/cdk_datapipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDatapipelineStack(app, "cdk-datapipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
