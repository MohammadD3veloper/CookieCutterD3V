"""
All the project random numbers will be declare in here.
These randoms can be used in anywhere of our project
"""

import random


def otp_code():
    return random.randrange(100000, 999999)
