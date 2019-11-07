# Lambda Function for attach or detach EBS volumes and Mount to Instance
import boto3
import paramiko
ec2 = boto3.resource('ec2') 
vol = ec2.Volume('vol-id')
# Detach-volume 
res = vol.detach_from_instance(Device='/dev/xvda', Force=True|False, InstanceId='i-09a37f61546ea0f9c')
print res
# Attach-volume 
attach = vol.attach_to_instance(Device='path', InstanceId='')
print attach
# Authintication to Ec2 Ianstance and Mount Ebs
k = paramiko.RSAKey.from_private_key_file("your-pem-key")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect( hostname = "Dns",username = "user",pkey = k )
commands = [ "sudo mkdir -p /mnt/scott","sudo mount -t xfs -o nouuid divice-name path-to-mount" ]
for command in commands:
        print "Executing {}".format( command )
        stdin , stdout, stderr = c.exec_command(command)
        print stdout.read()
        print( "Errors")
        print stderr.read()
c.close()
