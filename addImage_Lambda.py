import base64
import boto3
import uuid

client = boto3.client('s3')

def lambda_handler(event, context):
        
       
        decoded_image_data = base64.b64decode(event['body'])
        
      
        filename = str(uuid.uuid4()) + '.jpg'
        
        # Generate the key with the "Images/" prefix
        key = f'Images/{filename}'
        
       
        bucket_name = bucket
        
   
        response=client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=decoded_image_data

        )
     
      
        return {
            'statusCode': 200,
            'body': {
                'message': 'Image uploaded successfully',
            }
        }
   