import boto3
import datetime
import json


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    now_in_utc = datetime.datetime.utcnow().isoformat()
    default_title = "N/A"
    jira_ticket = "N/A"
    dynamo = boto3.resource('dynamodb').Table(payload['times'])
    response = dynamo.put_item(
        started_at=now_in_utc,
        title=default_title,
        jira_ticket=jira_ticket
    )
    return respond(None, response)

