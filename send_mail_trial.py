import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

print 'sending email'
server.login("vtsproject006@gmail.com","vidya123")
mymsg = 'Message from Raspberry Pi'
server.sendmail("vtsproject006","patilnn22597@gmail.com",mymsg)
server.quit()
print 'email sent'
