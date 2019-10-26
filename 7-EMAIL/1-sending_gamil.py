import smtplib



smtpUser = 'projectjunkieslabs@gmail.com'
smtpPass = 'project123!'

subject = 'Mail from RPI 3'

toAdd = 'datheshraghu@gmail.com'
fromAdd = smtpUser


header = 'TO:' + toAdd + '\n' +'From:' + fromAdd + '\n' + 'Subject:' + subject + '\n'
body = ' Hi Pal How are you !'

print header + '\n' + body



s = smtplib.SMTP('smtp.gmail.com',587) #SMTP server With port 587 or 465

s.ehlo() # it is for ESMTP server

s.starttls() # Transport Layer security anthing after this is encrypted

s.login(smtpUser, smtpPass) # Login With your Account

s.sendmail(fromAdd, toAdd, header + '\n' + body)



s.quit()
