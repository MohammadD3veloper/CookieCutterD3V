"""
All the project regexes will be declare in here.
These regexes can be used in somewhere of our project
eg: models, forms, serializers
"""

import re


def phone_number_regex(phone_number):
    """ Checking phone number validation by regex """
    return re.match("^09[1-2-3]+{11}", phone_number)
