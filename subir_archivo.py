import boto3
import base64
import json

def lambda_handler(event, context):
    body = event.get('body')
    if isinstance(body, str):
        body = json.loads(body)

    bucket = body['bucket']
    directorio = body['directorio']
    nombre_archivo = body['nombre_archivo']
    contenido_base64 = body['contenido']

    s3 = boto3.resource('s3')
    s3.Object(bucket, f"{directorio}/{nombre_archivo}").put(Body=base64.b64decode(contenido_base64))

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': f'Archivo {nombre_archivo} subido correctamente a {bucket}/{directorio}'
        })
    }