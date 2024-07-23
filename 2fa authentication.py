import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# List of valid passwords
passwords = ["Lemmy", "Morton", "Roy", "Wendy", "Iggy", "Junior", "Ludwig", "Larry"]#can change if you want

# Loop to handle password attempts
while True:
    password = input("Enter the password: ")
    
    if password in passwords:
        # Get the email address for sending the 2FA code
        email_address = input("Enter your email address: ")

        # Email account credentials (for demonstration; in production, use environment variables)
        sender_email = "...@aaa.com"# insert username and password for email address which sends the mfa message
        sender_password = "password"  

        subject = "2FA Password"

        # Generate a random number for 2FA
        random_no = random.randint(1, 99)
        body = f"The special number is {random_no}"

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the server
            server = smtplib.SMTP('smtp.office365.com', 587)#change for appropriate email server and port no.
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to your email account
            
            # Send the email
            server.sendmail(sender_email, email_address, msg.as_string())
            
            # Close the server connection
            server.quit()
            
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")

        # Prompt the user to enter the 2FA code
        try:
            FA2_number = int(input("Enter the number emailed to you: "))
            
            if FA2_number == random_no:
                print("Correct - you're in!")
                break  # Exit the loop upon successful 2FA
            else:
                print("Wrong number - access denied!")
        except ValueError:
            print("Invalid input - please enter a valid number.")
    
    else:
        print("Wrong password. Please try again.")
