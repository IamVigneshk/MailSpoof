import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_smtp_server(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as connection:
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def send_mail(receiver_email, spoofed_email, spoofed_name, message, subject, smtp_host, smtp_port, smtp_username, smtp_password):
    try:
        msg = MIMEMultipart("related")
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(spoofed_email, receiver_email, text)
        server.quit()
        print(f'Spoofed Email sent successfully to {receiver_email} from {spoofed_name}')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

spoofed_email = 'guncity11@gmail.com'
spoofed_name = 'Ganesh Reddy Karri'
smtp_file_path = '/Users/vigneshk/Documents/GitHub/GSPoof/smtp_configurations.txt'

smtp_configurations = []
with open(smtp_file_path, 'r') as file:
    for line in file:
        smtp_host, smtp_port, smtp_username, smtp_password = line.strip().split(';')
        smtp_configurations.append({
            'host': smtp_host,
            'port': int(smtp_port),
            'username': smtp_username,
            'password': smtp_password
        })

receiver_email = 'vigneshk1432@gmail.com'
message = 'Your Leave Has been Approved'
subject = 'Re:Leave'

for config in smtp_configurations:
    smtp_host = config['host']
    smtp_port = config['port']
    smtp_username = config['username']
    smtp_password = config['password']
    
    print(f"Checking SMTP server {smtp_host}:{smtp_port}...")
    if check_smtp_server(smtp_host, smtp_port):
        print(f"SMTP server {smtp_host}:{smtp_port} is live. Attempting to send email...")
        if send_mail(receiver_email, spoofed_email, spoofed_name, message, subject, smtp_host, smtp_port, smtp_username, smtp_password):
            break
    else:
        print(f"SMTP server {smtp_host}:{smtp_port} is not available. Moving to the next server...")
