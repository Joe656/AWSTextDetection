import json
import boto3

def lambda_handler(event, context):

        cookie_Id = event['cookieId']
        image_data = event['imageFile']

       
        rekognition_client = boto3.client('rekognition')

        
        response = rekognition_client.detect_text(Image={'Bytes': image_data})

       
        unique_text_list = []
        for text in response['TextDetections']:
            if 'DetectedText' in text:
                detected_text = text['DetectedText']
                if detected_text not in unique_text_list:
                    unique_text_list.append(detected_text)
        # sends to add book
        api_endpoint = end
        payload = {
            'textData': unique_text_list,
            'cookieId': cookie_Id
        }
        
        json = json.dumps(payload)
        
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(api_endpoint, data=payload_json, headers=headers)
        
        return {
            'statusCode': 200,
            'body': 'Text detection completed successfully'
        }
    