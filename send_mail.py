import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'cce8110075ccb4'
    password = 'c4291e75f9f6f0'
    message = f"""<h3> New Feedback Submission </h3>
                <ul>
                    <li> Customer: {customer} </li>
                    <li> Dealer: {dealer} </li>
                    <li> Rating: {rating} </li>
                    <li> Comments: {comments} </li>
                </ul>"""

    sender_email = "example_sender@gmail.com"
    receiver_email = "example_receiver@gmail.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
