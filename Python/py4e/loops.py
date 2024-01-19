#Tutorial
# print('Hello! My name is Dev & I am glad to be a part of this course.')
# d = "Hello " + "there"
# print(d)
# e = d + '1'
# print(e)
# name = input("Who are you?")
# print('Welcome!',name)
# -------------------------------------------------------------------------------

#Assignment 2.3
#get data
# hours = input("Working Hours?")
# rph = input("Rate per hour?")

# #convert to int
# hours = int(hours)
# rph = float(rph)

# print('Pay:', hours * rph)
# -------------------------------------------------------------------------------

#Assignment 3.1
# hrs = input("Hours Worked?")
# rph = input("Rate per Hour?")

# try:
#     hours = float(hrs)
#     rate = float(rph)

#     if hours <= 40:
#         grosspay = hours * rate
#     else:
#         extra = hours - 40
#         grosspay = (40 * rate) + (extra * rate * 1.5)
#     print("Gross Pay:", grosspay)
# except:
#     print("Invalid Amount")
# -------------------------------------------------------------------------------

# #Assignment 3.3
# score = input("What's your score?")
# try:
#     grade = float(score)
#     if grade > 1:
#         print("Please enter score in range.")
#     elif grade >= 0.9:
#         print("A")
#     elif grade >= 0.8:
#         print("B")
#     elif grade >= 0.7:
#         print("C")
#     elif grade >= 0.6:
#         print("D")
#     else:
#         print("F")
# except:
#     print("Please enter a valid score.")
# -------------------------------------------------------------------------------

#Assignment 4.6
# hrs = input("Hours Worked?")
# rph = input("Rate per Hour?")

# try:
#     hours = float(hrs)
#     rate = float(rph)
#     def computepay():
#         if hours <= 40:
#             grosspay = hours * rate
#         else:
#             extra = hours - 40
#             grosspay = (40 * rate) + (extra * rate * 1.5)
#         return grosspay
#     print('Pay ', computepay())
# except:
#     print("Invalid Amount")
# -------------------------------------------------------------------------------

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('End')
# -------------------------------------------------------------------------------

#Assignment 5.1
# count = 0
# sum = 0

# while True:
#     storage = input("Enter a Number: ")
#     try:
#         house = float(storage)
#         count = count + 1
#         sum = house + sum
#         average = sum / count        
#     except:
#         if storage == "Done":
#             break
#         print("Invalid Amount")
#         continue    
# print('Total:', sum, 'Count:', count, 'Average:', average)
# -------------------------------------------------------------------------------

#Assignment 5.2

min = None
max = None

while True:
    storage = input("Enter a Number: ")
    try:
        house = float(storage)
        if min is None:
            min = house
        if min > house:
            min = house
        if max is None:
            max = house
        if max < house:
            max = house       
    except:
        if storage == "Done":
            break
        print("Invalid Amount")
        continue    
print("Maximum is", max)
print("Minimum is", min)