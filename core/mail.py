import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(keywords):
    # Email configuration
    sender_email = 'fridayro706@gmail.com'
    sender_password = keywords
    receiver_email = str(input("Enter receiver's email address: "))
    subject = str(input("Enter subject: "))
    body = str(input("Enter body: "))

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print('Error sending email:', str(e))