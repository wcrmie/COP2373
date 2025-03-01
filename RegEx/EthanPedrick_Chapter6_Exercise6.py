# This program uses RegEx to identify the validity of phone numbers, social security numbers, and zip codes.

import re

# Set up RegEx identifiers for each data type
phone = r"\d\d\d[ -]\d\d\d[ -]\d\d\d\d$"

sso = r"\d\d\d[ -]\d\d[ -]\d\d\d\d$"

zipcode = r"\d\d\d\d\d$"

def main():

    validatePhone()

    validateSso()

    validateZip()

    print("Your information all seems to be valid.")

def validatePhone():
    # Get the user's information
    uPhone = input("What is your phone number? (Format with separators as such: 555-555-5555) ")

    # While loop to allow user to input correctly
    while bool(re.fullmatch(phone, uPhone)) != True:
        print("Be sure to format your input properly.")
        uPhone = input("What is your phone number? (Format with separators as such: 555-555-5555) ")
    else:
        print("Input Accepted!")

def validateSso():

    uSso = input("What is your Social Security number? (Format with separators as such: 555-55-5555) ")

    while bool(re.fullmatch(sso, uSso)) != True:
        print("Be sure to format your input properly.")
        uSso = input("What is your Social Security number? (Format with separators as such: 555-55-5555) ")
    else:
        print("Input Accepted!")

def validateZip():

    uZip = input("What is your Zip code? ")

    while bool(re.fullmatch(zipcode, uZip)) != True:
        print("Be sure to format your input properly.")
        uZip = input("What is your Zip code? ")
    else:
        print("Input Accepted!")

main()
