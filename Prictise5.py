# print number from 1 to 100

'''i = 1 
while  i <= 100:
    print(i)
    i += 1

print("Question One is Solve!")
'''
# print number from 100 to 1

'''i = 100

while i >= 1:
    print(i)
    i -= 1

print("Question two is Solve!")
'''


# 3 ka table

'''i = 1
while i <= 10:
    print(3 * i)
    i += 1

print("Question three is Solve!")
'''


'''n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

print("your answer is complete!")'''


# print numbers using loop
'''nums = [1, 4, 6, 13, 17, 19, 23, 41, 53, 69, 71, 89, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

print("Question four is Solve!")'''


'''friends = ["Ali", "Raza", "Akif", "Adnan", "Owais", "Hamza", "Hassan",]
idx = 0

while idx < len(friends):
    print(friends[idx])
    idx +=1 

print("your friends list is print!")'''



# search number

'''nums = (1, 3, 4, 6, 13, 17, 19, 23, 41, 53, 69, 71, 89, 100, 101, 110, 120)

x = 6

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("your number is FOUND this index:", i)
    i += 1'''



# break loop


'''i = 1
while i <= 10:
    print(i)
    if(i == 7):
        break
    i +=1

print("loop is break number", i)
'''



'''tupp = ("a", "b", "c", "e", "x", "y", "z", "m", "j", "o", "l", "i")

alfh = "m"
i = 0

while i < len(tupp):
    if(tupp[i] == alfh):
        print("this alfha is FOUND",alfh )
        break
    else:
        print("finding")
    i += 1
'''


# continue
# current iteration main kuch skip karna hai wahan continue laga do, wo skip kar k aagay walim condition ya number print karwa dega
# # jis condition par continue lagay gay wo num print nai ho gaa aagay k saray numbers print ho jay gaa
'''i = 1

while i <= 15:
    if(i == 10):
        i +=1
        continue # 10 ko print nai kare gaa 11 se continue ho jay gaa
    print(i)
    i +=1
'''


# odd number ko print karna hai event ko skip 

'''i = 1

while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
'''

# event number ko print karna hai odd ko skip 

'''i = 1

while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
'''




#print list num using for loop

'''list = [1, 3, 5, 7, 9, 13, 19, 27, 35, 47, 53, 69, 73, 88, 91, 100]

for nums in list:
    print(nums)

print("All Number is Print")
'''


# search number x in this tupple using for loop

'''tupp = (1, 3, 5, 7, 9, 13, 19, 27, 35, 47, 53, 69, 73, 88, 91, 100,)

x = 27

#index b add kar sakte hai
idx = 0

for numbers in tupp:
    if(numbers == x):
        print(x, "is found at idx:", idx)
        break
    idx += 1'''


# print number 1 to 100

'''for i in range(1, 101):
    print(i)
'''


# print number 100 to 1

'''for i in range(100, 0, -1):
    print(i)
'''


# Table
'''n = int(input("input number: "))

for i in range(1, 11):
    print(n * i)
'''

# tolat sum of user number using while loop

'''n = int(input("input any number for sum: "))   
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Tolat Sum is =",sum)
'''




# tolat sum of user number for loop
'''n = int(input("input any number for sum: "))

sum = 0

for i in range(1, n+1):
    sum += i

print("Tolat Sum is =",sum)
'''



# factorial using while
'''n = int(input("input any number:"))
fac = 1
i = 1


while i <= n:
    fac *= i
    i += 1

print("this number factorial is = ", fac)'''



# factorial using for

'''n = int(input("input any number:"))
fac = 1


for i in range(1, n+1):
    fac *= i

print("this number factorial is = ", fac)
'''
