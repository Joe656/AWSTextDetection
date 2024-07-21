import base64
import boto3
import mysql.connector



client = boto3.client('s3')

def lambda_handler(event, context):
 
       
    request_body = json.loads(event['body'])
    text_Data = request_body.get('textData', [])
    cookie_Id = request_body.get('cookieId', '')
    endpoint=end

    username=user
    password=pw
    database_name=db
    connection = mysql.connector.connect(host=endpoint,user=username,passwd=password,db=database_name)
    cursor = connection.cursor()
    
      
    query = "INSERT INTO imagesite.Books (userID,description) VALUES (%s,%s)"
    cursor.execute(query,(cookie_Id,text_Data))
            
    connection.commit()
    cursor.close()
    connection.close()
    print("Event:", event)
       
       
        return {
            'statusCode': 200,
    
            }
        }

