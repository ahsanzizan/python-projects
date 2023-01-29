# SEND EMAIL WITH AN ATTACHMENT IN IT

import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
SENDER = "my@gmail.com"
RECEIVER = "your@gmail.com"
PASSWORD = "sender password"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = SENDER
message["To"] = RECEIVER
message["Subject"] = subject
message["Bcc"] = RECEIVER  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as att:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    base = MIMEBase("application", "octet-stream")
    base.set_payload(att.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(base)

# Add header as key/value pair to attachment part
base.add_header("Content-Disposition", f"attachment; filename= {filename}")

# Add attachment to message and convert message to string
message.attach(base)

# Log in to server using secure context and send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, ssl.create_default_context()) as s:
    s.login(SENDER, PASSWORD)
    s.sendmail(SENDER, RECEIVER, message.as_string())
