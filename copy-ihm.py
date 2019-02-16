import boto3
import paramiko
def worker_handler(event,context):
        s3_client = boto3.client('s3')
        # Download the private key file from secure S3 bucket
        s3_client.download_file('mybucket-isow-family', 'ISOWKEYPAIR.pem', '/tmp/ISOWKEYPAIR.pem')

        k = paramiko.RSAKey.from_private_key_file("/tmp/ISOWKEYPAIR.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        host = "34.207.128.136"
        print("Connecting to Host :",host)
        c.connect( hostname = host, username = "ec2-user", pkey =k)
        print("Connected to :",host)

        commands = [
                "ls -ail",
                "ps -ef"
                ]
        return
        {
                'message' : "Script execution completed. See Cloudwatch logs for complete output"
        }