import smtplib, ssl
import os

def send_mail(message):
    global host, port, username, password, context, server
    host = "smtp.gmail.com"
    port = 465
    username = "nguyenphong011978@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "nguyenphong011978@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
if __name__ == "__main__":
    send_mail("hi")


