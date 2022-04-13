import uuid
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import boto3

session = boto3.session.Session(profile_name='er')
dynamodb = session.client('dynamodb', region_name='us-east-1')

# create a table if not exists
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
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )#.meta.client.get_waiter('table_exists').wait(TableName='users')
except dynamodb.exceptions.ResourceInUseException:
    pass

app = Flask(__name__)
api = Api(app)

class User(Resource):
    # id = str(uuid.uuid4().hex)[:8]
    # id = '123456'
    def get(self, uid):
        try:
            response = dynamodb.get_item(
                TableName='users',
                Key={
                    'uid': {
                        'S': uid
                    }
                }
            )
            return {'uid': response['Item']['uid']['S']}, 200
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404

    def post(self, uid):
        # parser = reqparse.RequestParser()
        # parser.add_argument('uid', type=str, required=True, help='id cannot be blank')
        # args = parser.parse_args()
        # id = args['uid']
        print(id)
        try:
            dynamodb.put_item(
                TableName='users',
                Item={
                    'uid': {
                        'S': uid
                    }
                }
            )
            return {'uid': uid}, 201
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404
    
    def put(self, uid): # update
        try:
            dynamodb.update_item(
                TableName='users',
                Key={
                    'uid': {
                        'S': uid
                    }
                },
                UpdateExpression="set password = :val1",
                ExpressionAttributeValues={
                    ':val1': {
                        'S': 'changed_password'
                    }
                },
            )
            return {'uid': uid}, 204
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404

    def delete(self, uid):
        try:
            dynamodb.delete_item(
                TableName='users',
                Key={
                    'uid': {
                        'S': uid
                    }
                }
            )
            return '', 204
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404
        
class UserList(Resource):
    def get(self):
        try:
            response = dynamodb.scan(
                TableName='users'
            )
            for item in response['Items']:
                return {'uid': item['uid']['S']}, 200
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404


api.add_resource(User, "/user/uid=<string:uid>",
                methods=['GET', 'POST', 'PUT', 'DELETE'])
api.add_resource(UserList, '/users',
                methods=['GET'])

# Driver function
if __name__ == "__main__":
    app.run(debug=True)
