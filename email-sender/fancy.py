# SENDING HTML BASED EMAIL

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER = "sender@gmail.com"
RECEIVER = "receiver@gmail.com"
PASSWORD = "sender password"

message = MIMEMultipart("alternative")
message["Subject"] = "Testing"
message["From"] = SENDER
message["To"] = RECEIVER

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain or html MIMEText objects
first_part = MIMEText(text, "plain")
second_part = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(first_part)
message.attach(second_part)

# Create secure connection with server and send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, ssl.create_default_context()) as s:
    s.login(SENDER, PASSWORD)
    s.sendmail(SENDER, RECEIVER, message.as_string())
