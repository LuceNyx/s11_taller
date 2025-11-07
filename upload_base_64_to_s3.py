import base64
import boto3

def upload_base_64_to_s3(s3_bucket_name, s3_file_name, base_64_str):
    """
    Allows for the upload of a base64 string to a s3 object, may need fleshing out down the line, returns location
    of file in S3
    :param s3_bucket_name: S3 bucket name to push image to
    :param s3_file_name: File name
    :param base_64_str: base 64 string of the image to push to S3
    :return: Tuple of bucket_name and s3_file_name
    """
    s3 = boto3.resource('s3')
    s3.Object(s3_bucket_name, s3_file_name).put(Body=base64.b64decode(base_64_str))
    return (s3_bucket_name, s3_file_name)