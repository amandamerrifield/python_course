#module: a Python file containing reusable components (functions/classes )
# standard library : a suite of modules that comes with Python
# third party modules can present problems because you're dependent on how well this thing is written 
# maintenance of 3rd party stuff can be questionable as well
# A suite of standard modules lives here : https://docs.python.org/3/library/index.html
# we will be working with regular expressions here
# regular expressions is a pattern for matching against text (regex for short)

import re

def check_email():
    email = "stuartb@stayahead.com"
    pattern = "[A-z]+@[A-z]+\\.[A-z]+" # this is NOT a good email pattern 

    is_valid = re.match(pattern, email)

    if is_valid:
        print("valid email")
    else:
        print("fix email pls")

import datetime as dt 
def check_normans():
    today = dt.date(2024, 1, 31)
    norman_conquest = dt.date(1066, 10, 14)
    print(today-norman_conquest)

#---

import os

def check_directory():
    os.mkdir("my_dir")
    files = os.listdir(".")
    for file in files:
        print(file)

# ---
        
import json 

def json_import():
    people = [
        {"name": "Tom"},
        {"name": "Dick"},
        {"name" : "Harry"}
    ]
    json_people = json.dumps(people)
# ---

import requests

def request_and_response():
    response = requests.get("https://bbc.co.uk")
    print(response.content)