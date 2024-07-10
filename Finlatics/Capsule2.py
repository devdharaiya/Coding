## Q1) Write a program that prompts the user to input a year, checks whether it's a leap year or not, and then prints the result.
# while True:    
#     raw = input("Enter the Year to check:")
#     year = int(raw)
#     if year % 4 == 0:
#         print("Year:", year)
#         print("Leap Year:", "Yes")
#     else:
#         print("Year:", year)
#         print("Leap Year:", "No")


## Q2) Write a Python program that prompts the user to input a word. The program should then determine and output the count of vowels (a, e, i, o, u) in the provided word. Additionally, consider that the word can be in either uppercase or lowercase.
# word = input("Please enter a word:")
# check = word.lower()
# count = 0
# vowels = ['a','e','i','o','u']
# for i in check:
#     if i in vowels:
#         count = count + 1
# print("No. of vowels in given word:", count)


## Q3) Write a Python program that allows the user to input a list of 6 names. After receiving the list, the program should print only the names that start with the letter 'a', regardless of whether the letter is uppercase or lowercase.
# names = list()
# while True:
#     if len(names) == 6:
#         break
#     else:
#         ask = input("Enter a name:")
#         names.append(ask)
# for i in names:
#     if i.startswith('a') or i.startswith('A'):
#         print(i)

## Q4) Write a Python program that takes a list of 10 integers as input. Your program should iterate through the list and print the following:
## For each even number encountered, print the number squared.
## For each odd number encountered, print the number cubed.
# integers = list()
# while True:
#     if len(integers) == 10:
#         break
#     else:
#         ask = int(input('Please Enter an Integer:'))
#         integers.append(ask)
# for i in integers:
#     print('Original Number:', i)
#     print('Squared Number:', i * i)
#     print('Cubed Number:', i * i * i)

## Q5) Imagine you're ordering flowers from a local delivery service. They offer a selection of beautiful flowers, including roses. Each rose is priced at Rs. 10. Along with your choice of roses, you'll need to provide the count of roses you wish to order and the delivery distance. The delivery charges are as follows: Rs. 25 for distances within 5 kilometers, Rs. 50 for distances between 5 and 10 kilometers, and Rs. 75 for distances greater than 10 kilometers. Write a Python program that prompts the user to enter the count of roses and the delivery distance, then calculates and displays the total price to pay, including both the cost of roses and the delivery charge.
# count = int(input('How many roses do you wish to buy:'))
# dist = int(input('Delivery Distance:'))

# if dist <= 5:
#     distCost = 25
# elif dist > 5 and dist <= 10:
#     distCost = 50
# else:
#     distCost = 75
# print('Total Cart Value: Rs. 10 X', count, 'Qty:', count * 10)
# print('Delivery Cost:', distCost)
# print('Total Charges:', count * 10 + distCost)
