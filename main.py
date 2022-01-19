import smtplib
import os

email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_id, email_pass)

    subject = 'Fight Against CoronaVirus'
    body = 'Hey, hi, lets fight against coronavirus together by staying at home and following covid protocols.'

    msg = f'Subject : {subject}\n\n{body}'

    smtp.sendmail(email_id, '195543@nith.ac.in', msg)
