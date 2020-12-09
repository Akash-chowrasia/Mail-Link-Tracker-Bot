import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
f1 = open("dummymaillist.csv")
csvreader = csv.reader(f1, delimiter=',')
i=0
for row in csvreader:
    a = [f'{row[0]}']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Server Link catcher program"
    msg['From'] = "sender@gmail.com"
    msg['To'] = a[0]
    html="""
    <!DOCTYPE html>
<html lang = "en">
<head></head>
<body>
<a href="http://127.0.0.1:9000">Go to my new website project</a><br>
</body>
</html>
    """
    part = MIMEText(html, 'html')
    msg.attach(part)
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("sender@gmail.com","senderPassword")
        smtp.sendmail("sender@gmail.com", a[0], msg.as_string())
        i+=1
        print(i)
