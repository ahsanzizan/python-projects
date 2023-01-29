# SENDING PLAIN TEXT EMAIL
import smtplib, ssl

port = 1025  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
password = "sender password"
message = """\
Subject: Testing

This message is sent from Python."""

with smtplib.SMTP_SSL(smtp_server, port, ssl.create_default_context()) as s:
    s.login(sender_email, password)
    s.sendmail(sender_email, receiver_email, message)
