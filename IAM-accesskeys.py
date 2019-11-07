import boto3
iam = boto3.client('iam')
accesskey = iam.create_access_key(UserName='user-name')
print(accesskey['Accesskey'])
