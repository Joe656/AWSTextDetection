import mysql.connector
import json

def lambda_handler(event, context):
    
    endpoint = end
    username = user
    password = pw
    database_name = db

    connection = mysql.connector.connect(host=endpoint, user=username, passwd=password, db=database_name)
    cookieID = event.get('cookieId', '')
    

        cursor = connection.cursor()
        query = 'SELECT description FROM imagesite.Books WHERE userID = %s'
        cursor.execute(query, (cookieID,))

        rows = cursor.fetchall()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(rows)
        }
        cursor.close()
        connection.close()
