import boto3, json

def lambda_handler(event, context):
    # Aseguramos que el body sea un diccionario
    body = event.get('body')
    if isinstance(body, str):
        body = json.loads(body)

    bucket_name = body['bucket']

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Bucket {bucket_name} creado exitosamente'})
    }