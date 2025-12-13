
file_name = "email.txt"

from emails import email_sender, email_recipient, email_subject, email_body

with open(file_name, 'r', encoding='utf-8') as file:
    email_text = file.read()

print("Sender:", email_sender(email_text))
print("Recipient:", email_recipient(email_text))
print("Subject:", email_subject(email_text))
print("Email body:\n", email_body(email_text))