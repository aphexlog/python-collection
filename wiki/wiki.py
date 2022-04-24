import wikipediaapi
import boto3

wiki = wikipediaapi.Wikipedia('en')

# Get a wiki page by title
page = wiki.page('List of countries by GDP (PPP) per capita')
# print(page.text)

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('wiki')
# print(table.table_status)


# table.put_item(
#     Item={
#         'test_page': page.title,
#         'test_name': page.text
#     }
# )
# print(table.table_status)

table.put_item(
   Item={
        'pages': 'this is a test',
        'name': page.title,
        # 'url': page.fullurl
    }
)

print(table.table_status)
