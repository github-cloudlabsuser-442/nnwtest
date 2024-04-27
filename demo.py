import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if validate_email(email):
    # Proceed with further code
    print("Email is valid!")
else:
    print("Invalid email address. Please try again.")


  # validate phone number using international phone number format
def validate_phone_number(phone):
    """
    Validates a phone number.

    Args:
        phone (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    pattern = r'^\+\d{1,3}\s\d{1,14}$'
    if re.match(pattern, phone):
        return True
    else:
        return False
        

    