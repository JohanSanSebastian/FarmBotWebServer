# ALERT: WIP AND HIGHLY UNSTABLE :)

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "farmbotstatus@yahoo.com"
receiver_email = "johantestbot@gmail.com"
password = input("Type your password and press enter:")

# Create the plain-text and HTML version of your message
text = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">DAMN FARMBOT UPDATE, ur welcome bhau bhau</a>
    </p>
  </body>
</html>
"""

def send_email():
    message = MIMEText(text, "html")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    mail = smtplib.SMTP("smtp.mail.yahoo.com", 465)
    mail.starttls()
    mail.login(sender_email, password)
    mail.sendmail(sender_email, receiver_email, message.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()