import smtplib
from email.message import EmailMessage

def alert_system(product, link):
    email_id = 'travelshravel7@gmail.com'
    email_pass = 'India101'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'travelshravel7@gmail.com' # send to self
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)