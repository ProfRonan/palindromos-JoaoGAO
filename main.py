"""Main functions"""


def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = string.lower()
    string = ''.join(c for c in string if c.isalnum())
    if string == string[::-1]:
     return True
    else:
     return False
