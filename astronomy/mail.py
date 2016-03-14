# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText('lala')
# fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents'
msg['From'] = 'letyrodri@gmail.com'
msg['To'] = 'letyrodri@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail('letyrodri@gmail.com', ['letyrodri@gmail.com'], msg.as_string())
s.quit()
