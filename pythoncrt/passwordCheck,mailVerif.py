# read password as input from user and check it is valied or invalid
# read password as input from user and check it is valid or invalid with all credentials
password = input("Enter your password: ")

# Define the minimum length
length = 10
uppercase = 0
lowercase = 0
digit = 0
special = 0

# Iterate through the password to check for character types
for char in password:
    if char.isupper():
        uppercase = 1
    elif char.islower():
        lowercase = 1
    elif char.isdigit():
        digit = 1
    elif not char.isalnum():  # Check for special characters (not alphanumeric)
        special = 1

# Check if all criteria are met
if (len(password) >= length and
    uppercase == 1 and
    lowercase == 1 and
    digit == 1 and
    special == 1):
    print("Valid password")
else:
    print("Invalid password")
    print("Password must meet the following criteria:")
    print(f"- At least {length} characters long")
    print("Checks at least one uppercase letter")
    print("Checks at least one lowercase letter")
    print("Checks at least one digit")
    print("Checks at least one special character")
#read name contact number mailid and password and make sure that contact number has 10 digits and mail should have valid strucrure name @orgname.comand password should have atleast 3 uppercase alp,3lowecase alpha,3 special characters and 1 number and password leng should not be less than 10


#read name contact number mailid and password and make sure that contact number has 10 digits and mail should have valid strucrure name@orgname.com and password should have atleast 3 uppercase alp,3lowecase alpha,3 special characters and 1 number and password length should not be less than 10
# read name, contact number, mailid, and password with validation

name = input("Enter your name: ")
contact_number = input("Enter your contact number: ")
mail_id = input("Enter your mail ID: ")
password = input("Enter your password: ")
if len(contact_number) == 10 and contact_number.isdigit():
    print("Contact number is valid.")
else:
    print("Invalid contact number. Please enter 10 digits.")
if "@" in mail_id and "." in mail_id.split("@")[-1]:
    print("Mail ID is valid.")
else:
    print("Invalid mail ID structure.")
min_length = 10
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

for char in password:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isalnum():
        special_count += 1

if (len(password) >= min_length and
    uppercase_count >= 3 and
    lowercase_count >= 3 and
    special_count >= 3 and
    digit_count >= 1):
    print("Password is valid.")
else:
    print("Invalid password.")
    print("Password must meet the following criteria:")
    print(f"At least {min_length} characters long")
    print("Contain at least 3 uppercase letters")
    print("Contain at least 3 lowercase letters")
    print("Contain at least 3 special characters")
    print("Contain at least 1 digit")
    