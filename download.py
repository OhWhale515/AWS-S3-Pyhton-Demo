import os 
import boto3

#client
client = boto3.client('s3')

# path variables
bucket =  'sgreen515-s3-demo'
cur_path = os.getcwd()
file = 'CloudResume.docx'
filename = os.path.join(cur_path, 's3files', file)

# object download method
client.download_file (
    Bucket=bucket,
    Key=file,
    Filename=filename
)

# list s3 contents
downloads_dir = os.path.join(cur_path, 's3files')

for root, dirs, files in os.walk(downloads_dir):
    for fn in files:
        print(fn)