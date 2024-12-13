# 2FA Password Verification System

This Python script implements a simple two-factor authentication (2FA) system where users need to provide a valid password followed by a code sent via email. The system uses a list of predefined valid passwords and generates a 2FA code, which is sent to the user's email. To successfully authenticate, the user must enter the correct password and the correct 2FA code sent to their email.

## Features
- **Password Verification**: Users must enter one of the predefined valid passwords to begin the 2FA process.
- **Email Integration**: After successful password entry, a 2FA code is sent to the user's email address.
- **2FA Code Verification**: The user must enter the correct 2FA code to gain access.
- **Error Handling**: Includes checks for incorrect password entries and invalid 2FA code inputs.

## Requirements

- Python 3.x
- `smtplib` library (for sending emails)
- `email.mime.multipart` and `email.mime.text` libraries (for creating the email structure)

To install any missing dependencies, you can use the following command:
```bash
pip install secure-smtplib
```

## Usage

1. **Run the script**:
   Run the Python script to start the 2FA process.

2. **Enter the password**:
   Enter one of the valid passwords from the predefined list. If correct, the system will ask for your email address to send the 2FA code.

3. **Provide an email address**:
   The system will send a 2FA code to the entered email address.

4. **Enter the 2FA code**:
   Check your email inbox for the 2FA code and input it into the system. If the code is correct, you will be granted access.

5. **Access Denied**:
   If the wrong password or incorrect 2FA code is entered, access will be denied.

## Example

```bash
Enter the password: Morton
Enter your email address: user@example.com
Email sent successfully!
Enter the number emailed to you: 23
Correct - you're in!
```

## Configuration

To use this script, you will need to configure the following:

1. **Sender Email**:
   - Modify the `sender_email` variable to your email address (the address that will send the 2FA email).
   - Modify the `sender_password` variable to the password of the sender email account.
   - Ensure you are using the correct SMTP server and port for your email provider (`smtp.office365.com` and port `587` for Office 365).

2. **Email Provider**:
   - If you're using a different email provider, adjust the SMTP server and port accordingly.

3. **Password List**:
   - The `passwords` list contains predefined valid passwords. You can modify this list to add or remove passwords as needed.

## Notes

- Make sure you enable "Less secure app access" or the necessary security settings for your email account if you're using Gmail or other providers.
- This system is for demonstration purposes and should not be used in production environments without proper security measures.
