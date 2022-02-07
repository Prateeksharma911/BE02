import json
import boto3
import env

def sns():
    topicArn = "arn:aws:sns:us-east-1:484958538548:practo"
    snsClient = boto3.client(
        "sns",
        aws_access_key_id = env.accessKey,
        aws_secret_access_key = env.secretKey,
        region_name='us-east-1'
    )
    publishObject = { "productId": 659 ,"amount": 9700 }
    response = snsClient.publish(TopicArn=topicArn,
                                Message=json.dumps(publishObject),
                                Subject="Product",
                                MessageAttributes={"ProductType":{"DataType":"String","StringValue":"Product"}})
    print(response['ResponseMetadata']['HTTPSStatusCode'])
def sqs():
    client = boto3.client('sqs', region_name='us-east-1',
                    aws_access_key_id="ACCESS KEY GOES HERE ", 
                    aws_secret_access_key="SECRET KEY GOES HERE ")
    QueueUrl = "https://queue.amazonaws.com/484958538548/pacto"
    response = client.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0)
    print(response)


if __name__ == "__main__":
    sns()
    sqs()
