import json
import boto3 
#--------------------------------------------imports json and boto3 modules 
dynamodb = boto3.resource('dynamodb') 
#--------------------------------------------grabs DynamoDb context
table = dynamodb.Table('VisitorTable') 
#--------------------------------------------grabs my Ddb table
def lambda_handler(event, context): 
  #------------------------------------------specifies a lambda handler with two arguments
  response = table.get_item(Key={'Key_id':'0'}) 
  #-------------------------------------------grab item by its key id
  print(response)
  #-------------------------------------------If response is empty, make visitor_count record starting at 1, return visitor_count
  if not response.get("Item"):
      print("null")
      visitor_count = 1
      table.put_item(Item={'Key_id':'0', 'visitor_count':visitor_count})
      response = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        "body": {'count': visitor_count},
        "isBase64Encoded": 'false'
    } 
      return response
  else:
      print("full")
  #-------------------------------------------if response has an item, save to visitor_count, iterate by 1, and update the record
  visitor_count = response['Item']['visitor_count']
  #-------------------------------------------save the value of the item as visitor_count
  visitor_count = visitor_count + 1
  #-------------------------------------------increment the visitor_count to reflect current page load
  response = table.put_item(Item={'Key_id':'0', 'visitor_count':visitor_count})
  #-------------------------------------------update Ddb with new visitor_count value
  response = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        "body": {'count': visitor_count},
        "isBase64Encoded": 'false'
    }
  return response
  #-------------------------------------------return the visitor_count to be handled by JS
