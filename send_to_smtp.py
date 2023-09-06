import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    fromaddr = data["fromaddr"]
    toaddr = data["toaddr"]
    mypass = data["mailpass"]
    reportname = "log.txt"

msg = MIMEMultipart
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Hello"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part["Content-Disposition"] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

body = "Test"
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
