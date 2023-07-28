# age = 30
# print(age)

#Use variables with snake casing
#We write capital letters in Python for a variable so as to indicate that variable 
#is not meant to change.

# 12/3 will give 4.0
# 12//3 will give 4, it ignores everything after the decimal 

# integer_division = 13//5
# print(integer_division)

#finding out the remainder
# remainder = 13%5
# print(remainder)
#====================================
# Strings
# age=23
# print(str(age))
# print(f'You are {age} years of age')

#getting inputs
# my_name = "Joe"
# your_name = input("Enter your name: ")
# your_age = int(input("Enter your age: "))
# print(f"Hello {your_name} sir.Your age is {your_age*12}")

# default_greeting = "there"
# name = input("Enter your name: (optional)")
# user_name = name and default_greeting
# print(f'Hello,{user_name}')

#============================================
# List
# friends1 = ["olf","Bob","Anne"]
# print(len(friends1))
# friends2 = [["olf",23],["Bob",22],["Anne",14]]
# print(friends2[0][0])
# friends3 = [
#     ["olf",23],
#     ["Bob",22],
#     ["Anne",14],
#     ["Rosh",26],
#     ["Box",22]
#     ]
# friends1.append("Jen")
# print(friends1)
# friends3.remove(["Box",22])
# print(friends3)
#=========================================
#TUPLE
# short_tuple = "Rolf","Bolb"
# a_bit_clear = ("Rolf","Bob")
# tuple_in_list = [("Rolf","Bolb")]
# a_tuple = "Rolf",
# friends1 = ("olf","Bob","Anne")
#We cannot add element using 'append'
# friends1 = friends1 + ("Jen",) #We can add 2 tuples together
# print(friends1) 
#===================================
# SETS: no order, no duplicates
# art_friends = {"Rolf","Anne"}
# science_friends = {"Jen","Charlie"}
# art_friends.add("Jen")
# print(art_friends)
# art_friends.remove("Jen")
# print(art_friends)
# art_friends = {"Rolf","Anne","Jen"}
# science_friends = {"Jen","Charlie"}
# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science)
# art_friends.add("pixie")
# We do not append in sets since sets do not have any order.
# print(art_friends)

# science_but_not_art = science_friends.difference(art_friends)
# print(science_but_not_art)

# not_in_both = art_friends.symmetric_difference(science_friends)
# print(not_in_both)

# art_and_science = art_friends.intersection(science_friends)
# print(art_and_science)

# all_friends = art_friends.union(science_friends)
# print(all_friends)

#DICTIONARY
#allows you to store keys and values and is usefull when you know the key.
# friend_ages = {"Rolf":24,"Adam":30,"Anne":23}
# print(friend_ages["Rolf"])

#Assigning the values
# friend_ages["Anne"]=90
# print(friend_ages["Anne"])

# print(friend_ages)
#Difference between dictionaries and set  is that dictionary do keep the order in
# which u added the keys.
# We cannot have duplicate keys in dictionary
# friends = (
#     {"name":"Rolf Smith", "age":24},
#     {"name":"Adam Wool", "age":29},
#     {"name":"Anne Pun", "age":28}
# )

# print(friends[0]['name'])
# print(friends[1]['name'])
# print(friends[2]['name'])

#Conversion
# friends = [("Rolf",23),("Adam",20),("Anne",10)]
# friend_ages = dict(friends)
# print(friend_ages)

#Length and sum
# grades = [80,75,90,100]
# total = sum(grades)
# print(total)
# print(len(grades))
# print(total/len(grades))

#If you do not want to add more elements to your collection , use tuple otherwise 
#use List.(in case of grades storage)

#JOIN
# friends = ["Rolf","Anne","Charlie"]
# comma_seperated = ",".join(friends)#Each value will be taken and formed a string with commas.
# print(comma_seperated)

#if 
# friend = "Rolf"
# user_name = input("Enter your name: ")
# if user_name == friend:
#     print("Hello, friend!")
# else:
#     print("Hello,stranger!")    
# print("This runs away")    

# if 4:
#     print("Runs.")

# friends = ["Rolf","Bob","Anne"]
# family = ["Jen","Charlie"]

# user_name = input("Enter your name: ")
# if user_name in friends:
#     print("Hello, Friend!")

# if (user_name in family):
#         print("Hello, family")    
# else:
#     print("I don't know you.")   

#While loops

# user_input = input("Do you wish to run the program ? (yes/no)")

# while user_input == "yes":
#     print("You are learning")
#     user_input=input("Do you wish to run the program?(yes/no)")

# print("We stopped running")
#########################################
#for-loop
# friends = ['abb','cdd','eff','ghh']
# for friend in friends:
#     print(friend) 
# for _ in friends:
#     print(_)

# for i in range(5,10):
#     print(i)

# students = (
#     {"name":"Rolf Smith", "age":24},
#     {"name":"Adam Wool", "age":29},
#     {"name":"Anne Pun", "age":28}
# )  
# for student in students:
#      print(student['name'])
#      print(student['age'])

#DESTRUCTURING
# currencies = 0.8,1.2
# usd,eur = currencies
# print(usd)

# friends = [("Rolf",25),("Anne",24),("Charlie",31),("Bob",11)]
# for name,age in friends:
#     print(name,age)

# friend_ages = {"Rolf":21,"Anne":23,"Charlie":12,"Bob":22}
# # for name in friend_ages:
# #     print(name)   
# for age in friend_ages.values():
#     print(age)     
# for name,age in friend_ages.items():
#     print(name,age)      

#Break And Continue
cars = ["ok","ok","ok","faulty","ok","ok"]
# for status in cars:
#     print(status)
#     if(status == "faulty"):
#         print("Stopping the production line")
#         break #terminating the loop completely
# for status in cars:
#     print(status)
#     if(status == "faulty"):
#         print("Found the faulty car , skipping...")
#         continue #skipping the iteration.
#============================================
#else keyword
# cars = ["ok","ok","ok","faulty","ok","ok"]
# for status in cars:
#     if status == "faulty":
#         print("Stopping the production line!")
#         break
#     print(status)
#     print("Shipping new car to customers!")
# else:
#     print("All cars built successfully.No faulty cars")  
# #else means that if entire loop runs without an error , then else block will
# # get executed.      
#=====================================
#Prime numbers using for loop
# for n in range(2,10):
#     for x in range(2,n):
#         if (n%x)==0:
#             print(f'{n} equals {x} * {n//x}')
#             break
#     else:
#         print(f'{n} is prime')
#==============================================
friends = ['abb','cdd','eff','ghh']
# print(friends[2:4])  
# print(friends[1:])      
# print(friends[:4]) 
# print(friends[:])#here we get a new list not the same list.
# print(friends[-3:4])
# print(friends[-3:])#both have same result
# print(friends[:-2])
# print(friends[-2:])
# print(friends[-4:-2])
#=================================================
numbers = [0,1,2,3,4]
doubled_numbers = []
# for number in numbers:
#     doubled_numbers.append(number*2)
# print(doubled_numbers)

#using list comprehension for above given problem 
# doubled_numbers = [number *2 for number in numbers]
# print(doubled_numbers)
# doubled_numbers = [number *2 for number in range(5)]
# print(doubled_numbers)

# friend_ages = [22,31,35,37]
# age_strings = [f'My friend is {age} years old.'for age in friend_ages]
# print(age_strings)

# names = ["Rolf","Bob","Anne","John"]
# lower = [name.lower() for name in names]
# print(lower)

# friend = input("Enter your friend name: ")
# friends = ["Rolf","Bob","Anne","John"]
# friends_lower = [name.lower() for name in friends]
# if friend.lower() in friends_lower:
#     print(f'{friend.title()} is one of your friends.')

#==============================================
#List Comprehension
# ages =[22,23,24,25,26,27]
# odds = [age for age in ages if age%2==1]
# print(odds)

# friends = ["Rolf","Bob","Anne","John"]
# guests  = ["jose","Bob","Rolf","Charlie","Michael"]

# friends_lower =set([name.lower() for name in friends])
# guests_lower = set([guest.lower() for guest in guests])

# print(friends_lower.intersection(guests_lower))

# # 2nd Approach
# present_friends = [
#     name.title() for name in guests if name.lower() in friends_lower
# ]
# print(present_friends)
#===================================================
#Set comprehension
# friends = ["Rolf","Bob","Anne","John"]
# guests  = ["jose","Bob","Rolf","Charlie","Michael"]

# friends_lower = {n.lower() for n in friends}
# guests_lower =  {n.lower() for n in guests}

# present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
# print(friends_lower.intersection(guests_lower))
# print(present_friends)

#Dictionary Comprehension
# friends = ["Rolf","Bob","Anne","John"]
# time_since_seen = [3,7,5,11]
# long_timers = {
#     friends[i]:time_since_seen[i]
#     for i in range(len(friends))
#     if(time_since_seen[i]>5)
# }
# print(long_timers)
#=================================================
#ZIP function
# friends = ["Rolf","Bob","Anne","John"]
# time_since_seen = [3,7,5,11]

# # dict([("Rolf",3),("Bob",7),("Jen",15),("Anne",11)])
# long_timers = dict(zip(friends,time_since_seen))#will combine both and results in list of tuples
# print(long_timers)
# #with zip we can combine lists
#==================================================
# #ENUMERATE
# friends = ["Rolf","John","Anna"]
# # for i in enumerate(friends):
# #     print(i)
# # print(list(enumerate(friends)))  
# # print(list(zip([0,1,2],friends)))  #which is equivalent to enumerate
# print(dict(enumerate(friends,start=1)))#start=1 will start the numbers from 1.
#===================================================
#FUNCTIONS
# def greet():
#     name=input("Enter your name: ")
#     print(f"Hello, {name}")
# greet()    
# #variable created inside the function die when they reach end of the function.
#==============================================

# def calculate_mpg(car_to_calculate):
  
#     mpg = car_to_calculate["mileage"]/car_to_calculate['fuel_consumed']
#     name = f'{car_to_calculate["make"]}{car_to_calculate["model"]}'
#     print(f'{"name"} does {mpg} miles per gallon)')

# calculate_mpg({
#     "make":"Ford",
#     "model":"Fiesta",
#     "mileage":230,
#     "fuel_consumed":450
# })
# cars = [
#     {"make":"Ford","model":"Fiesta","mileage":23000,"fuel_consumed":460},
#     {"make":"Ford","model":"Focus","mileage":17000,"fuel_consumed":350},
#     {"make":"Mazda","model":"MX-5","mileage":49000,"fuel_consumed":900},
#     {"make":"Mini","model":"Cooper","mileage":31000,"fuel_consumed":235}

# ]
# def calculate_mpg(car_to_calculate):
  
#     mpg = car_to_calculate["mileage"]/car_to_calculate['fuel_consumed']
#     return mpg
# def car_name(car_to_calculate):
#     name = f'{car_to_calculate["make"]}{car_to_calculate["model"]}'
#     return name
# def print_car_info(car):
#     name = car_name(car)
#     mpg = calculate_mpg(car)
#     return (f'{"name"} does {mpg} miles per gallon)')

# for car in cars:
#    print(print_car_info(car))
#=============================================
# Default parameter
# def add(x,y=6):#default value is defined here
#     total = x+y
#     return total

# print(add(12))
# #we can also define it as 
# print(add(x=12))
# print(add(x=12,y=13))
# print(add(11,y=13))
#============================================
#seperator
# print(1,2,3,4,5,6,sep='-')
#============================================
#Lambda functions
# def divide(x,y):
#     return x/y
# #lambda conversion
# divide:lambda x,y:x/y
# print(divide(15,3))
# #=========================================
# # def average(sequence):
# #     return sum(sequence)/len(sequence)
# #Lambda conversion
# average = lambda sequence:sum(sequence)/len(sequence)

# students = [
#     {"name":"Rolf","grades":(12,23,34,45)},
#     {"name":"Bob","grades":(11,21,31,41)},
#     {"name":"Jen","grades":(12,22,32,42)},
#     {"name":"Rolf","grades":(12,23,34,45)},
# ]
# for student in students:
#     print(average(student["grades"]))

#Lambda functions are used for getting input and returning outputs and not used 
# for performing actions such as what the print function does.
#=============================================
#First class functions
def greet():
    print("Hello")

hello = greet #Now hello and greet are the same value


















