from crypt import methods
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
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    ).meta.client.get_waiter('table_exists').wait(TableName='wiki')
except dynamodb.exceptions.ResourceInUseException:
    pass

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, username):
        try:
            id = str(uuid.uuid4().hex)[:8]
            response = dynamodb.get_item(
                TableName='users',
                Key={
                    'username': {
                        'S': username
                    },
                    'id': {
                        'S': id
                    }
                }
            )
            return {'username': response['Item']['username']['S'], 'id': response['Item']['id']['S']}, 200
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404

    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        id = args['id']
        try:
            dynamodb.put_item(
                TableName='users',
                Item={
                    'username': {
                        'S': username
                    },
                    'id': {
                        'S': id
                    }
                }
            )
            return {'username': username, 'id': id}, 201
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404

    def delete(self, username):
        try:
            dynamodb.delete_item(
                TableName='users',
                Key={
                    'username': {
                        'S': username
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
                return {'username': item['username']['S']}, 200
        except dynamodb.exceptions.ResourceNotFoundException:
            return {'error': 'User not found'}, 404


api.add_resource(User, "/user/<string:username>",
                methods=['GET', 'POST', 'DELETE'])
api.add_resource(UserList, '/users',
                methods=['GET'])

# Driver function
if __name__ == "__main__":
    app.run(debug=True)
