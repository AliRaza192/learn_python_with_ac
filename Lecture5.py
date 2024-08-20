# LOOPS in Python
# kisi kaam ko repeat karna hai to looping karte hain

# While loop
# while ka matlab jab tak ye condition true ho tum work karte raaho


'''i = 1 # isko iterator kehtay hain
while i <= 9 :
    print(i,"LOOPs") # is looping ko iteration kehtay hain
    i += 1

print(i)
'''


# 1 se 50 tak number print karwane ka tariqa 

'''i = 1 
while i <= 50:
    print(i)
    i += 1

print("Loop Ended")
'''

# 5 se 1 tak 
'''i = 5 
while i >= 1:
    print(i)
    i -= 1

print("Loop Ended")

'''


#FOR LOOP in Python

# sequence main travel karna 
# sequence se sare numbers print ho gay

# for loop in list
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for el in numbers:
    print(el)
'''

# for loop in tupple

'''foods = ("Biryani", "Qorma", "Karaie", "Pilao")

for item in foods:
    print(item)
'''

# for loop in tupple
# for loop k bad hum else ko opitional b print karwa sakte hai
'''str = "AliRaza"

for character in str:
    print(character)

else:
    print("for loop END")
'''

# kisi loop main break ko use karna ho to wahan else ki zarorat parhti hai, agr sirf print likhe gay to print statment run ho jay gi


'''name = "Muhammad"

for br in name:
    if(br == "h"):
        print("h is found")        
        break
    print(br)
else:
    print("not found")
'''

# age else nai likhte phir b last wala print statement chalay gaa
'''name1 = "Muhammad"

for br in name1:
    if(br == "h"):
        print("h is found")        
        break
    print(br)

print("not found")'''


#Range in for loop
# range by defualt 0 se start hoti hai,
# range main 3 value hoti hai (start?, stop, step?)
# starting or steping value optional hoti hain , stoping value compulsory 
# step value ka matlab kitny number se value increase karni hai

'''seq = range(10)

for i in seq:
    print(i)
'''

#normaly range ko isi tariqay se likhte hain
'''for i in range(20): # stop value
    print(i)'''


'''for i in range(5, 15): # start and stop value
    print(i)
'''

'''for i in range(2, 20, 2 ): # start, stop and step value , 
    print(i)
'''


# even number print

'''for i in range(2, 101, 2):
    print(i)
'''

# odd number print

'''for i in range(1, 100, 2):
    print(i)
'''


#Pass in loop
# pass ka matlab loop ko empty chor doo
# empty is liye chorty hain k humay bad main code karna hota hai

'''for i in range(10):
    pass

print("empty loop working...")
'''
# agr pass na likhe or loop ko aasay hi chor day to error aayega

'''for i in range(10):
    #empty 

print("empty loop working...") # error: expected an indented block 
'''

