import smtplib
from email.mime.text import MIMEText

def sendEmail(emailFrom, emailTo, subject, body,
    login, password, smtpServer, smtpPort):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = emailFrom
    msg['To'] = ';'.join(emailTo)
    server = smtplib.SMTP_SSL(smtpServer, smtpPort)
    server.login(login, password)

    problems = server.sendmail(emailFrom, emailTo,  msg.as_string())
    server.quit()