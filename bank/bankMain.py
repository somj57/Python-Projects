from bankDetails import *

myObj = bank()
myObj._setDetails("SBI", "Bheem Sharma", "2020202", "121212ANL", "1221" )
# print(f'This is illegal : {myObj.Balance}') # This is illegal
print()
myObj1 = bank()
myObj1._setDetails("RBI", "Bheem Sharma", "2020202", "121212ANL", "1221" )

myObj1.printDetails()
myObj.printDetails()