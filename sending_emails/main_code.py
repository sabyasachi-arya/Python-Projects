import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir/Madam,
This a sample email which is sent by Pyhton. I hope you like it.
1. Python is Named After a Comedy Show
Python isn’t named after the snake. 
It’s actually named after the British comedy group Monty Python. Guido van Rossum, 
the creator of Python, wanted a name that was short,
 unique, and slightly mysterious — and he was a big fan of Monty Python's Flying Circus.

2. Readability is Sacred
Python's design philosophy emphasizes code readability.
It uses indentation (spaces or tabs) instead of braces {} to define blocks of code —
which is quite rare in programming languages.

3. Used by Big Names
Python is used by top companies like Google, Netflix, NASA, and Instagram. 
In fact, YouTube was largely written in Python during its early development.

4. It’s Great for Game Development Too
Python can be used to build games.
The Pygame library allows developers to create 2D games easily — 
it's often used by beginners to learn programming in a fun way.

5. You Can Write AI with Just a Few Lines
Python is the go-to language for Artificial Intelligence and Machine Learning. 
With libraries like TensorFlow, PyTorch, 
and Scikit-learn, you can build an AI model in under 10 lines of code.
Thank you.


Kind regards,
Sabyasachi Bhattacharjee
'''


email = EmailMessage()

email['Subject'] = 'Test Email'
email['From'] = 'saby@sandboxe004848f10f14ddbadc5f69391ac0438.mailgun.org'
email['To'] = 'sabyasachi.arya@gmail.com'

email.set_content(email_content)


smtp_connector = smtplib.SMTP(host='smtp.mailgun.org', port=587)
smtp_connector.starttls()
smtp_connector.login('saby@sandboxe004848f10f14ddbadc5f69391ac0438.mailgun.org', '0147224a8d0b78c6001a3490fcd25cdb-e71583bb-8142766d')

smtp_connector.send_message(email)
smtp_connector.quit()