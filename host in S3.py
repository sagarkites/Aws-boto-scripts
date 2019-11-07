# Lambda Function for Enabling static web-hosting with HTML pages
import boto3
s3 = boto3.client('s3')
web = {'ErrorDocument':{'Key':'error.html'},'IndexDocument':{'Suffix':'index.html'}}
upload_file = s3.put_bucket_website(Bucket='sagarscott',
                                      WebsiteConfiguration=web)
print(upload_file)
get = s3.get_bucket_website(Bucket='bucket')
File1 = s3.upload_file('local-file-path','your-bucket-name','index.html')
File2 = s3.upload_file('local-file-path','your-bucket-name','error.html')
print(File1)
print(File2
