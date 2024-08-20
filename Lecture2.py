# strings

# string ko teno tarah likh sakte hain
'''str1 = 'Ali'
str2 = "Ali"
str3 = """Ali"""
'''


# Escope sequence characters

# \n line break karne k liye aata hai
'''str4 = "this is string value. \nwe are creating it in python."
print(str4)
'''

# \t tab speace add karne k liye aata hai
'''str5 = "this is string value. \twe are creating it in python."
print(str5)
'''


# concatenation

'''x = "Ali"
y = "Raza"
name = x + " " +  y # len main speace b count hoti hai
print(len(name))
print(name)'''



# Indexing
'''ind = "Lecture_Two"
print(ind[2])'''


#index main sirf value ko access kar sakte hain, change nai kar sakte 
'''ind1 = "Python"
ind1[0] = "B"
print(ind1) #error  TypeError: 'str' object does not support item assignment
'''


#Slicing
    #accessing part of string
# slicing format straring inx : ending inx
# slicing main star wala inx shamil or end wala nai

#positive indexing
'''slc = "Course Of Python"
print(slc[6 : 9])

print(slc[: 9]) # start wali value nai di to iska matlab [0:9]
'''

#ye dono same hai
'''print(slc[10:])
print(slc[10:len(slc)])'''


#negative indexing
    #     5- -1 
'''neg = "apple"
print(neg[-3: -1]) 
'''

# other functions
# string ka end agr same hoga to true warna false return kare gaa
'''fun = "lecture"
print(fun.endswith("re")) #same True
print(fun.endswith("ab"))  #Falsw
'''

#capitalize
'''str = "i am studing python"
print(str.capitalize())
'''

#replace
'''str = "i am studing python"
print(str.replace("python", "javaScript"))
'''
#fine
'''str = "i am studing python" 
print(str.find("python")) # hmare str main jahan par python pehli baar aa raha hai fine iska index num nikal kar dega
'''

#count

'''str = "this is my leacture num 2"
print(str.count("i")) # i hamare str main kitni baar aaya hai isko count karega
print(str.count("my"))
'''


#Conditions statements

'''age = int(input("Enter your age for validation: "))

if(age >= 18):
    print("your age is valid for enrollment") # indentation 

else:
    print("your age is less than 18 you are not valid for enrollment")
'''


'''marks = int(input("Enter your marks: "))

if(marks >=90):
    print("Your Grade is 'A'")
elif(marks >= 80 and marks < 90):
    print("Your Grade is 'B'")
elif(marks >= 70 and marks < 80):
    print("Your Grade is 'C'")
elif(marks >= 60 and marks < 70):
    print("Your Grade is 'D'")
else:
    print("your are failed")'''



'''marks = int(input("Enter your marks: "))

if(marks >=90):
    grade =  "A"
elif(marks >= 80 and marks < 90):
    grade =  "B"
elif(marks >= 70 and marks < 80):
    grade =  "C"
elif(marks >= 60 and marks < 70):
    grade =  "D"
else:
    grade = "your are failed"

print("grade of the student ->", grade)'''




#Nesting 
#aik statement main dosri statement likhna nesting kehlata hai

age = int(input("Enter your age for driving : "))

if(age >= 18):
    if(age >=100):
        print("cannot drive your age is 100 0r plus..")
    else:
        print("can drive")
else:
    print("cannot drive your age is less than 18")













