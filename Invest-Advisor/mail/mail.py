import smtplib, base64
from email import *
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Mail:
    __password = 'UmFzcGJlcnJ5UGlfYXRfSW52ZXN0QWR2aXNvcg=='
    __email = 'dailyinvestadvisor@gmail.com'

    __subject = 'Tägliche Aktien-Analyse'
    __msg = MIMEMultipart('related')
    __html = 'Nothing'

    __images = []

    def __init__(self, receiverMails) -> None:
        self.__receiverMails = receiverMails
        self.__msg.set_charset("utf-8")
        self.__msg['Content-type'] = 'text/plain; charset=utf-8'
        self.__msg['From'] = self.__email
        self.__msg['Subject'] = self.__subject

    def send(self):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        self.__msg.attach(MIMEText(self.__html, "html"))

        for img in self.__images:
            self.__msg.attach(img)

        base64_bytes = self.__password.encode('ascii')
        password_bytes = base64.b64decode(base64_bytes)
        password = password_bytes.decode('ascii')

        smtp.login(self.__email, password)
        for receiverMail in self.__receiverMails:
            self.__msg['To'] = receiverMail
            smtp.sendmail(self.__msg['From'],self.__msg['To'],self.__msg.as_string())
        smtp.quit()
        print('send')

  
    #in HTML: <img src="cid:logo"/>
    def addImage(self, image, imageName):
        fp = open(image, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<{name}>'.format(name=imageName))
        self.__images.append(msgImage)
    
    def addHtml(self, html):
        self.__html = html