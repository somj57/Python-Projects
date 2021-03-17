# import constantData
# print(constantData.pi)
# constantData.pi = 1212
# print(constantData.pi)

# Formating the Strings
# a = 'aaaaaa'
# b ='bbbbbbbb'
# print('{1}ccccc{0}'.format(a,b))
# print(f'cccc{a}ccccc{b}')

# a = [1,1,1,12,2,3,13,121,21,2,1,212,12,1,2]
# b = set(a)
# print(b)
# a = b
# print(a)

# Implicit and Explicit Type Casting
# iVar = 10
# fVar = 12.50
# tVar = iVar + fVar
# print(type(tVar))
# fVar1 = int(fVar)
# tVar1 = iVar + fVar1
# print(type(tVar1))
# iVar = 10
# sVar = "som"
# sVar = int(sVar)
# tVar = iVar + sVar
# print(type(tVar),tVar)

# Input method
# _collegeName = input("Enter Your Collage Name : ")
# print(_collegeName)

# email = input("Enter EmailId: ")
# splitted = email.split('@')
# domain = splitted[-1]
# name = splitted[0].replace('.',' ')
# print('Domain: ',domain)
# print('name: ',name)

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)

# print('1111:''software'*3)

# num = int(input("Enter any number : "))
# if num > 10:
#     print("yehhhh")
# elif num == 10:
#     print("yoooyoyooy")
# else:
#     print("nooooooo")
# print('Over')

# proffesionList = ['engnr','doctor','ca']
# for proffesion in proffesionList:
#     print(proeffsion)
    
# # Arrays
# import array as arr
# a = arr.array('i', [1, 2, 3]) 
# print ("The new created array is : ", end =" ") 
# for i in range (0, 3): 
#     print (a[i], end =" ") 
# print()

# Largest number from an array collection
# import array as arr
# a = arr.array('i', [12,322,4,43,121,555,3321,543]) 
# b = list(a)
# print(max(b))

# max1 = a[1]
# n = len(a)
# for i in range(0,n):
#     if max1<a[i]:
#         max1 = a[i]
# print(max1)

# List are Mutable
# a = [12,2,2,2]
# a[2] = 4

# List Functions
# a = [1,2,12,54,422,112,34]
# print(f'{sorted(a)}')
# print(f'{max(a)}')
# a.remove(112)
# print(a)


# l = (1,2,3,4,5)
# l.pop()

# a = {}
# print(type(a))

# a=5
# b=10
# a,b = b,a
# print(a,b)

# import time
# time.sleep(2)
# print('lol')

# Function 3 key features
# 1) Redundency
# 2) Flexilibity
# 3) Maintainablity
 
# A function is known as with various names like:
#   -> Methods
#   ->sub-routine
#   ->procedure

# def _showMorningGreetings():
#     print("Good Morning ")
# def _showEveningGreetings():
#     print("Hey How are you")
# _showMorningGreetings()
# _showEveningGreetings()

# Types of function in python
# 1) Default argumented
# 2) Positional argumented
# 3) Arbitrary argumented

# def _login(_userId = "tim", _userPassword = "123"):
#     print(f"Welcome {_userId}")
#     print(f"Password {_userPassword}")
# _login("tim","123")
# _login("123","tim")
# _login(_userId = "tim", _userPassword = "123")

# def _info (*_userId, **_hobbies):
#     print(f"Userd Id's {_userId}")
#     print(f"Hobbies : {_hobbies}")
# _info('12','121',circket="3",football="0")

# def _employeeInfo(*_employeeDetails):
#     for i in range (len(_employeeDetails[0])):
#         print(f"{_employeeDetails[0][i]} : {_employeeDetails[1][i]}")
#     print("Another Method")
#     for(empId, empNames) in zip(_employeeDetails[0],_employeeDetails[1]):
#         print(f"{empId} : {empNames}")

# empNames = ['a','b','c']
# empId = [1,2,3]

# _employeeInfo(empId,empNames)

# def _myfunction():
#     """
#     Namaste🙏🏻
#     """
#     pass
# _myfunction

# Global / Local variables
# x =100
# def _updatingGlobalVariable():
#     global x
#     x = 500
#     print(f'Updated value of x = {x}')
# print(f'Value of x is = {x}')
# _updatingGlobalVariable()
# print(f'At last x = {x}')

# Lambda functions
# _myVar = lambda a,b : (a+b)*2
# print(_myVar(10,20))

# import random as rd
# # _carToDrive = ["Honda", "Maruti", "Hyundai", "Mahindra"]
# # rd.shuffle(_carToDrive)

# print(rd.randint(1,20))

# print(f'{list(range(10,1,-2))}')

# How to make switch in python
# def week(i):
#     switcher = {
#         0:'Sunday',
#         1:'Monday',
#         2:'Tue',
#         3:'Wed',
#         4:'Thru',
#         5:'Fri',
#         6:'Sat',
#     }
#     return switcher.get(i, "Invalid Day Of The Week")
# print(f"{week(22)}")

# def _filterMovies(_movies):
#     _moviesLiberary = ["M1","M2","M3"]
#     if(_movies in _moviesLiberary):
#         return True
#     else:
#         return False
# _findMovies = ["M1","M2"]
# _filteredMovieObject = filter(_filterMovies, _findMovies)
# print(list(_filteredMovieObject))

# _moviesLiberary = ["M1","M2","M3"]
# _findMovies = ["M1","M2"]
# _filteredMovieObject = filter(lambda movies: movies in _moviesLiberary, _findMovies)
# print(list(_filteredMovieObject))
# print(type(_filteredMovieObject))

# def _findPercentage(_marksScored):
#     print(f"{_marksScored}")
#     return (_marksScored/1000)*100
# _yearMarks = (800,700,900,850)
# _resultMapObject = map(_findPercentage, _yearMarks)
# print(type(_resultMapObject))
# print(_resultMapObject)
# _percentages = list(_resultMapObject)
# print(_percentages)

# _yearMarks = (800,700,900,850)
# _totalMarks = (1000,800,1000,900)
# result = list(map(lambda marks,total: round(((marks/total)*100), 2), _yearMarks,_totalMarks))

# totalPercentage = 0
# for per in result:
#     # print(per)
#     totalPercentage  = totalPercentage + per
# totalPercentage = totalPercentage / 4
# print(totalPercentage)

# _tFristName = ("A1","A2","A3","A4")
# _tMiddleName = ("B1","B2")
# _tLastName = ("","C1","C3")
# _tMobile = ("D1","D2","D3")
# _zipObject = zip(_tFristName,_tMiddleName,_tLastName,_tMobile)
# print(tuple(_zipObject))






