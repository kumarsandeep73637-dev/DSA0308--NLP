import re

# Input text
text = "My email is naveen123@gmail.com and my phone number is 9876543210"

# Search email pattern
email_pattern = r'\w+@\w+\.\w+'

email = re.search(email_pattern, text)

if email:
    print("Email Found:", email.group())

# Find numbers
number_pattern = r'\d+'

numbers = re.findall(number_pattern, text)

print("Numbers Found:", numbers)
