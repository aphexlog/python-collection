import boto3

session = boto3.session.Session(profile_name='er')
dynamodb = session.client('dynamodb', region_name='us-east-1')

def create_table():
    try:
        dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'uid',
                    'KeyType': 'HASH'
                }
            ],

            AttributeDefinitions=[
                {
                    'AttributeName': 'uid',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
    except dynamodb.exceptions.ResourceInUseException:
        print('users table already exists')

if __name__ == '__main__':
    create_table()
