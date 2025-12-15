import re 

def email_sender(email_text):
    for line in email_text.splitlines():
        if line.startswith("From:"):
            match = re.search(r'<([^>]+)>', line)
            if match:
                return match.group(1)
    return None

def email_recipient(email_text):
    for line in email_text.splitlines():
        if line.startswith("To:"):
            match = re.search(r'<([^>]+)>', line)
            if match:
                return match.group(1)
    return None

def email_subject(email_text):
    for line in email_text.splitlines():
        if line.startswith("Subject:"):
            return line[len("Subject:"):].strip()
    return None

def email_body(email_text):
    parts = email_text.split("\n\n", 1)
    if len(parts) > 1:
        return parts[1].strip()
    return None
