import boto3
from botocore.config import Config

s3_client = boto3.client('s3',
                         endpoint_url="&&&&&&&&",
                         aws_access_key_id='&&&&&&&',
                         aws_secret_access_key='&&&&&&&&&&&&&&',
                         config=Config(s3={'addressing_style': 'path', 'signature_version': "v2"}))
buckets = s3_client.list_buckets()
objects = s3_client.list_objects_v2(Bucket='&&&&&&&&&&&&&&')
for obj in objects['Contents']:
    print(obj['Key'])


# download
for doc in docs:
    try:
        with open(doc.file.name, 'wb') as data:
            print('download file with id', doc.id)
            s3_client.download_fileobj('bucket-name', 'path/' + doc.file.name, data)
    except Exception as e:
        print(e)

# upload
for doc in docs:
    try:
        with open(doc.file.name, 'rb') as data:
            print('uploading file with id :', doc.id)
            file_name = doc.file.name.rsplit('/', 1)[1]
            s3_client.upload_fileobj(data, 'bucket-name',
                                     'path/' + file_name)
    except Exception as e:
        print(e)