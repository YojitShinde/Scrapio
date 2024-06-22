import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def mail():
    user = ''
    password = ''

    message = MIMEMultipart('alternative')
    message['From'] = user
    message['To'] = user
    message['Subject'] = 'H-1B Visa Open Slots'

    filename = "H1-B Slots.txt"
    file = MIMEApplication(open(filename, 'rb').read())
    file.add_header('Content-Disposition','attachment', filename = 'H1-B Slots.txt')
    message.attach(file)

    session = smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()

    session.login(user, password)

    text = message.as_string()
    session.sendmail(user, user, text)
    session.quit()
    print('Mail Sent')

    if os.path.exists("H1-B Slots.txt"):
        os.remove("H1-B Slots.txt")
    else:
        print("The file does not exist")