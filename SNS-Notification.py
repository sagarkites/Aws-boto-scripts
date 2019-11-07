# Lambda Function for sending the SNS Notification 
import boto3
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
list = ec2.describe_instances()
for i in list["Reservations"]:
    j = [sagar["InstanceId"] for sagar in i["Instances"]]
    k = [chanti["State"] for chanti in i["Instances"]]
    l = k[0]
    if l["Name"] == "running":
        shutdown = (ec2.stop_instances(InstanceIds=j))
        res = "The Running Instances {} are shutdowned".format(j)
        print(res)
        sub = sns.subscribe(TopicArn = 'ARN',
	                Protocol = 'email',
	                Endpoint = 'vidyasagarchintaluri@gmail.com')
        pub = sns.publish(Message = 'res', TopicArn ='ARN' )
