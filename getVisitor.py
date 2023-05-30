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
  if !response['Item']
      print("NO ITEM")
  else:
    print("ITEM IS TRUE")
  #-------------------------------------------print to console
  #visitor_count = response['Item']['visitor_count']
  #-------------------------------------------save the value of the item as visitor_count
  #visitor_count = visitor_count + 1
  #-------------------------------------------increment the visitor_count to reflect current page load
  #response = table.put_item(Item={'Key_id':'0', 'visitor_count':visitor_count})
  #-------------------------------------------update Ddb with new visitor_count value
  #return visitor_count
  #-------------------------------------------return the visitor_count to be handled by JS
