import smtplib, base64
from email import *
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Mail:
    __password = 'UmFzcGJlcnJ5UGlfYXRfSW52ZXN0QWR2aXNvcg=='
    __email = 'dailyinvestadvisor@gmail.com'

    __subject = 'Tägliche Aktien-Analyse'
    __body = ''
    __msg = MIMEMultipart('alternative')
    __html = '<html><body>'+__body+'</body></html>'

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

        base64_bytes = self.__password.encode('ascii')
        password_bytes = base64.b64decode(base64_bytes)
        password = password_bytes.decode('ascii')

        smtp.login(self.__email, password)
        for receiverMail in self.__receiverMails:
            self.__msg['To'] = receiverMail
            smtp.sendmail(self.__msg['From'],self.__msg['To'],self.__msg.as_string())
        smtp.quit()

  
    #in HTML: <img src="cid:logo.png"/> oder <img src="cid:logo"/>
    def addImage(self, image, imageName):
         with open(image, "rb") as fp:
            img = MIMEImage(fp.read())
            img.add_header("Content-ID", "<{}>".format(imageName))
            self.__msg.attach(img)
    
    def addHtmlPart(self, htmlPart):
        self.__body = self.__body + htmlPart