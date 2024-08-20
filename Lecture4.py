# Dictionary 
# dictionary main har tarah ka data aa sakta hai
# dictionary mutable hai, change kar sakte hain


'''info = {
    "name" : "Ali",
    "age" : 24,
    "learn" : "Python",
    "marks" : 90.5

}

print(info)
'''
# dictionary main list or tupple ko b add kar sakte hain

'''info1 = {
    "name" : "Raza",
    "age" : 24,
    "learn" : "JavaScript",
    "marks" : 90.5,
    "subject" : ["Data type", "Array", "Function", "Objects"],


}

print(info1)
'''

# dictionary main indexing nai hoti agr iski kis value ko access karna hai to key k name k sath access kare gay


# info1["name", "age", "marks"] 



# dictionary main changes ho sakte hai jese yahan par age ko change kiya hai

'''info1["age"] = 23
print(info1)
'''


#dictionary main kuch add b kar sakte hai

'''info2 = {
    "name" : "Raza",
    "age" : 24,
    "learn" : "JavaScript",
    "marks" : 90.5,
    "subject" : ["Data type", "Array", "Function", "Objects"],

}

info2["topic"] = "Dictionary in Python"
print(info2)'''



# khaali dictionary b likh sakte hain, phir is main kuch add b kar sakte hain


'''null_dict = {}
null_dict["python"] = "Dictionary" # add
print(null_dict)'''


# Nested Dictionary 
# dictionary main aik or dictionary

'''student = {
    "name": "Arif",
    "information": {
        "age": 25,
        "class": 12,
        "city": "Karachi",
        "marks": 80.12,
        "grade": "A"
    }
}

print(student)
print(student["information"])
'''

#nested dict se value nikalni hai 

# print(student["information"]["grade"])



# Dictionary Methods
# .keys se dictionary ki sari keys aa jay gi
# .value se dictionary ki sari value aa jay gi

student1 = {
    "name": "Arif",
    "information": {
        "age": 25,
        "class": 12,
    },
    "marks": {
        "marks": 80.12,
        "grade": "A"
    }
}

# print(student1.keys())
# print(student1.values())


# is dictionary ko type casting se list main b change kar sakte hain

# print(list(student1.keys()))

# print(list(student1.values()))

# print(list(student1.items()))

'''pairs = list(student1.items())
print(pairs[0])
'''




# GET Method
# key ki value ko dono tarah print karwa sakte hain , lykn  agr get methods se value ko access kare or wo hmari dictionary main exits nai karti to None retun hoga , jab k sirf [] wale main error hoga

'''print(student1["name"]) 
print(student1.get("name"))'''


# UPDATE Method

student1.update({"city": "Karachi"})
print(student1)

# yahan par name2 ko access kar rahe hai jo hmari dictionary main nai hai 

'''print(student1["name2"]) # ye error return kare gaa
print(student1.get("name2")) # ye None '''



# dictionary ki len b nikal sakte hai
# ye dono valid hain

'''print(len(student1))
print(len(list(student1.keys())))'''



# SET in Python
# set unordered hota hai, value tarteeb se print nai hoti
#set immutable hai, or set main uniqe value store karte hain
# set main aik jese value ingnore hoti hai

'''nums = {1, 2, 3, }
print(nums)
print(type(nums))
'''


# empty SET syntax

'''collection = {} # ye syntax dictionary ka hai 
print(type(collection))


collection1 = set() # ye syntax SET ka hai
print(type(collection1)) 

'''

# SETs to mutable hain, lykn SETs k element immutable hain
# SET Methods

'''collect1 = {1, 2, 3, "A", "B", "C"}
print(collect1)'''

# ADD
collect = set()

collect.add(1)
collect.add(0)
collect.add(2)
collect.add(9)
collect.add("Ali")
collect.add("Raza")
# print(collect)


#REMOVE
'''collect.remove("Ali")
print(collect)'''


#ClEAR
'''collect.clear()
print(collect)'''


#POP
# pop set main se koi b random value delete kar deta hai

'''print(collect.pop())
print(collect.pop())
print(collect.pop())
print(collect)'''



#UNION
#union do sets main jo uniuqe value hoti hai is ka aik new set banata hai
# set1 or set2 main 5 do baar aa raha hai lykn union maik 5 sirf aik bar aaya 

set1 = {1, 2, 3, 4, 5, 6}
set2 = {0, 9, 8, 7, 6, 5}
# print(set1.union(set2))


#INTERSECTION
# intersection set1 or set2 main jo comman(aik jese) value hai unko print karega

print(set1.intersection(set2)) # {5, 6} comman hai set1 or set2 main



