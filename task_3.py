import re

def normalize_phone(phone_number):
    # Removing all characters except numbers and '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Checking if the number starts with '+'
    if not phone_number.startswith('+'):
        # Adding the code '+38' if the number does not contain an international code
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number
    
    return phone_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS campaigns:", sanitized_numbers)