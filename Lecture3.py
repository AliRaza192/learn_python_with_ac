# LIST IN PYTHON
# list or array dono aik hi hai

'''marks = [10, 30, 90, 50, 60]
print(marks)
print(type(marks))
print(len(marks))
'''
# list main multiple type ka data store kar sakte hain, array main sirf aik hi type ka data aa sakta ha

# students = ["Ali", 24, 92.97, "Karachi", True]


# python main string immutable hota hai, change nai ho sakta, 
# jab k list mutable hota hai, is main changing ho sakti hai

'''student = ["Raza", "lahore", 25]
print(student[0])
student[0] = "Hamza"

print(student) #changes karne k bad new list ko print karwaya 
'''


# Slicing in list

'''num = [100, 300, 900, 500, 600]
print(num[1:4])
print(num[1:])
print(num[:4])

# negative indexing

print(num[-4: -1])
'''


# LIST METHODS

# append list k add main aik value add kar deta hai jese yahan par 1 ko end main add kiya hai
'''list = [9, 4, 5, 3]

list1 = ["b", "c", "a", "d", "e"]

list.append(1)
print(list)

list1.append("f")
print(list1)'''

#sort list ko tarteeb deta hai , 
# accending order ka maltab pehle choti value aayegi phir baari jese 0,1,2
# descending order ka maltab pehle baari value aayegi phir choti jese 2,1,0
# sorting main by defult accending hoti hai
# sorting num or str dono par apply hoti hai

#accending 
'''list.sort() 
print(list) #by defualt accending

list1.sort()
print(list1)'''


# descending
'''list.sort(reverse=True)
print(list)

list1.sort(reverse=True)
print(list1)
'''

#RESVERSE Method

'''list.reverse()
print(list)


list1.reverse()
print(list1)
'''


# INSERT methodshorting
# list main kahin b kuch add karna ho to is k liye insert use karte hain kis jagah add karna hai or kiya add karna hai ("kis jagah jese 3", "kiya jese 4")

'''list2 = [1, 2, 3, 5, 6]
list2.insert(3, 4)
print(list2)
'''

# remove and pop

'''list3 = [6, 5, 4, 3, 2, 1, 6]
list3.remove(6) # konsa num ya value ko remove karna hai 6 jahan par pehli baar aayega wahan se remove ho jay gaa jese yahan par pehla 6 remove or last wala baaqi hai
print(list3)

list3.pop(3) # konsa index delete karna hai
print(list3)'''




# TUPPLE IN PYTHON
# tupple or list taqriban same hai, lykn list mutable hoti hai, or tupple immutable hote hai

tupp = (1, 0, 2, 9, 3, 8)
print(tupp)
print(type(tupp))

#tuppel main jab b single value hogi use "coma , " se saparate karna hoga warna python us aik variable sumjhe gaa

tupp1 = (1) #yahan par humne ne single tupple ko coma , se saparate kiya python isy aik int value consider kar raha hai
print(type(tupp1))

tupp2 = (1,)
print(tupp2)
print(type(tupp2)) # ye sahi tariqa hai 


# TUPPLE method
# tupple main index ka matlab ye value konse se index num par hai jese 5 index num 1 par aa raha hai
tupp3 = (1, 5, 0, 2, 9, 0, 5,)
print(tupp3.index(5))

# count ka matlab ye num ya value tupple main kitne baar aaye hai
print(tupp3.count(0))
