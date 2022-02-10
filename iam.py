import boto3
import csv
import os
import boto3
from datetime import datetime, timezone
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def ListUsers(writer):
	iam_report={}
	client=boto3.client('iam',aws_access_key_id='AKIAQA3SUJXDWHSDUUVY',aws_secret_access_key='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')
	response=client.list_users()
	#print(response['Users'])
	for user in response['Users']:
		
		current_datetime = datetime.now(timezone.utc)
		age=(current_datetime-user['CreateDate']).days
		print(user['UserName'],user['CreateDate'],age)
		iam_report["UserName"]=user['UserName']
		iam_report['CreateDate']=user['CreateDate']
		iam_report['Days']=age

		writer.writerow(iam_report)


def email_ses_attachment_notification(file_name):


	
	SENDER = "surendrasuni1997@gmail.com"

	# Replace recipient@example.com with a "To" address. If your account 
	# is still in the sandbox, this address must be verified.
	RECIPIENT = "surendrasuni1997@gmail.com"

	# Specify a configuration set. If you do not want to use a configuration
	# set, comment the following variable, and the 
	# ConfigurationSetName=CONFIGURATION_SET argument below.
	#CONFIGURATION_SET = "ConfigSet"

	# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
	AWS_REGION = "us-west-2"

	# The subject line for the email.
	SUBJECT = "IAM UserList"

	# The full path to the file that will be attached to the email.
	ATTACHMENT = file_name

	# The email body for recipients with non-HTML email clients.
	BODY_TEXT = "Hello,\r\nPlease see the attached file for a list of IAM Users."

	# The HTML body of the email.
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h1>Hello!</h1>
	<p>Please see the attached file for a list of customers to contact.</p>
	</body>
	</html>
	"""

	# The character encoding for the email.
	CHARSET = "utf-8"

	# Create a new SES resource and specify a region.
	client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id='AKIAQA3SUJXDWHSDUUVY',aws_secret_access_key='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')

	# Create a multipart/mixed parent container.
	msg = MIMEMultipart('mixed')
	# Add subject, from and to lines.
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT

	# Create a multipart/alternative child container.
	msg_body = MIMEMultipart('alternative')

	# Encode the text and HTML content and set the character encoding. This step is
	# necessary if you're sending a message with characters outside the ASCII range.
	textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

	# Add the text and HTML parts to the child container.
	msg_body.attach(textpart)
	msg_body.attach(htmlpart)

	# Define the attachment part and encode it using MIMEApplication.
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())

	# Add a header to tell the email client to treat this part as an attachment,
	# and to give the attachment a name.
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

	# Attach the multipart/alternative child container to the multipart/mixed
	# parent container.
	msg.attach(msg_body)

	# Add the attachment to the parent container.
	msg.attach(att)
	#print(msg)
	try:
	    #Provide the contents of the email.
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        },
	       # ConfigurationSetName=CONFIGURATION_SET
	    )
	# Display an error if something goes wrong. 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])



def main():
	
	
	file_header = ['UserName','CreateDate', 'Days']
	file_name = "iamreport.csv"
	with open(file_name , 'w',newline='') as csv_file:
	    writer = csv.DictWriter(csv_file, fieldnames=file_header)
	    writer.writeheader()
	  
	    print("display all users and creation date")
	    ListUsers(writer)
	    email_ses_attachment_notification(file_name)
main()
 
