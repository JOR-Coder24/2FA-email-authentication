# 2FA-email-authentication

Overview:
This Python script implements a simple two-factor authentication (2FA) system using email verification. The user is first asked to provide a valid password from a predefined list. If the password is correct, a 2FA code is generated and sent to the user’s email address. The user must then enter the correct 2FA code to gain access.

Features:
Password-based authentication with a list of valid passwords.
Generation and sending of a random 2FA code to the user's email.
Simple email setup using SMTP (configured for Outlook/Hotmail).
Input validation for both the password and the 2FA code.


Prerequisites


Before running the script, make sure you have the following:

Python 3.x installed.
The smtplib and email libraries (pre-installed with Python).
Access to an Outlook/Hotmail account for sending the 2FA email.


Installation and Setup


Clone the repository or copy the script into your local environment.
Open the script and update the following variables:
sender_email: Your Outlook/Hotmail email address.
sender_password: Your email account's password (For production, use environment variables or a secure credential manager).
Ensure that the email address you enter is valid and has SMTP enabled.

Note-may need to disable Firewall to use properly
