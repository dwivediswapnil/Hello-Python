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
