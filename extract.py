import re

def extract_emails(html: str) -> list[str]:
    """
    Parses html (string) and returns a list of email addresses.
    """
    # Regex for email addresses (basic but works for most cases)
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    return re.findall(email_pattern, html)


