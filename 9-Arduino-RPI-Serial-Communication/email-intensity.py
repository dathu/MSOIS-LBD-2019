import smtplib  # it is a simple mail transfer protocol library for python and it is present by default
from email.mime.text import MIMEText  #Import the email modules we'll need here it is a text datatype

USERNAME = "projectjunkieslabs@gmail.com"
PASSWORD = "project123!"
MAILTO  = "datheshraghu@gmail.com"

msg = MIMEText(' Hello Partcipents How are you It is Morning. This is the body of the email')
msg['Subject'] = 'Mail from RPI 3. Switch off the Light This email subject'
msg['From'] = USERNAME
msg['To'] = MAILTO

server = smtplib.SMTP('smtp.gmail.com:587') #SMTP server With port 587 or 465
server.ehlo_or_helo_if_needed() # it is for ESMTP server connection
server.starttls() # Transport Layer security anthing after this is encrypted
#server.ehlo_or_helo_if_needed()
server.login(USERNAME,PASSWORD) # Login With your Account
server.sendmail(USERNAME, MAILTO, msg.as_string())
server.quit()  # it is for ESMTP server termination
