Venom1 is a Python script designed to send spoofed emails using multiple SMTP server configurations. The script allows the user to input the sender's name and email, as well as the message and subject to be sent. It then checks the availability of each SMTP server from a provided list and attempts to send the email using the first available server.

Features
Sends spoofed emails with customizable sender information.
Utilizes multiple SMTP server configurations to ensure email delivery.
Checks the availability of SMTP servers before attempting to send an email.
Sends emails with plain text content.
Requirements
Python 3.x
smtplib library (included in Python's standard library)
email library (included in Python's standard library)
Setup
Clone the repository:

git clone https://github.com/IamVigneshk/MailSpoof.git

cd MailSpoof


Prepare the SMTP configurations file:
Create a text file named smtp_configurations.txt.
Add your SMTP server configurations in the following format (one per line):
smtp_host;smtp_port;smtp_username;smtp_password

Example:
scss
Copy code
smtp.example.com;587;user@example.com;password123
smtp.anotherexample.com;587;user@anotherexample.com;password456

Usage
Run the script:

python venom1.py

Input prompts:

Enter sender's email: spoofed_email@example.com
Enter sender's name: Spoofed Name
Enter the file path of the SMTP configurations text file: smtp_configurations.txt
Enter receiver's email: receiver@example.com
Enter message: This is a spoofed email message.
Enter subject: Spoofed Email Subject

Script execution:

The script will check the availability of each SMTP server listed in smtp_configurations.txt.
Once an available server is found, the script will attempt to send the email.
If successful, the script will print a success message and terminate.
If unsuccessful, the script will print an error message and try the next server in the list

$ python venom1.py
Enter sender's email: spoofed_email@example.com
Enter sender's name: Spoofed Name
Enter the file path of the SMTP configurations text file: smtp_configurations.txt
Enter receiver's email: receiver@example.com
Enter message: This is a spoofed email message.
Enter subject: Spoofed Email Subject
Checking SMTP server smtp.example.com:587...
SMTP server smtp.example.com:587 is live. Attempting to send email...
Spoofed Email sent successfully to receiver@example.com from Spoofed Name

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This tool is intended for educational and authorized testing purposes only. Unauthorized use of this tool for malicious activities is strictly prohibited and may violate laws and regulations. The author is not responsible for any misuse of this tool.

