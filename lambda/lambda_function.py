import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='ap-south-2')
table = dynamodb.Table('cloud-resume-counter')

def lambda_handler(event, context):
    
    # Get current count
    response = table.get_item(Key={'id': '1'})
    print("Response:", response)
    
    item = response.get('Item', {})
    views = item.get('views', 0)
    
    # Increment count
    views = int(views) + 1
    
    # Update the count in DynamoDB
    table.update_item(
        Key={'id': '1'},
        UpdateExpression='SET #v = :val',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':val': Decimal(views)}
    )
    
    # Return the new count
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'views': views})
    }