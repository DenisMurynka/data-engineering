import json
import boto3
import urllib3

def lambda_handler(event, context):
    bucket_name = 'ua-alarms-stage'
    file_name = 'file_name.json'
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_name)
    http = urllib3.PoolManager()

    try:
        response = http.request('GET',
                                "https://api.ukrainealarm.com/api/v3/alerts/regionHistory?regionId=16",
                                headers={
                                    "accept": "application/json",
                                    "authorization": "API_CODE"
                                },
                                retries=False)


        if response.status == 200:
            data = json.loads(response.data.decode('utf-8'))
            obj.put(Body=json.dumps(data).encode('utf-8'))
            return {
                'statusCode': 200,
                'body': 'File uploaded successfully.'
                
            }
            
        else:
            return {
                
                'statusCode': response.status,
                'body': 'Failed to fetch data from API.'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
        
