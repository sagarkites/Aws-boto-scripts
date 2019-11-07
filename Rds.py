# Lambda Function for Provisioning the RDS DB-Instances with credentials
import boto3
rds = boto3.client('rds')
try:
	Db = rds.describe_db_instances()
	for i in Db['DBInstances']:
		print("%s@%S:%s %s") % (i['MasterUsername'], 
			                    i['Endpoint']['Addresses'],
			                    i['Endpoint']['Port'],
			                    i['DBInstancesStatus'])
except Exception as e:
    print(e)	
print("Creating Database") 
response = rsd.create_db_instance(
           DBInstanceIdentifier = 'New_rds'
           MasterUsername = 'user'
           MasterUserPassword = 'pass'
           DBInstanceClass = 'db.t2.micro'
           Engine = 'mysql'
           AllocatedStorage = 5)
print(response)
