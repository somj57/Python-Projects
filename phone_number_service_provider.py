'''
pip3 install phonenumbers
'''

import phonenumbers
from phonenumbers import carrier

mobileNo = input('Enter number : ')

service_provider = phonenumbers.parse(mobileNo)
print(carrier.name_for_number(service_provider,"en"))
