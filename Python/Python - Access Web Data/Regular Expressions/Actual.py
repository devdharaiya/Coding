import re
# textNum = list()
# numbers = list()
# fhandle = open("Python/Python - Access Web Data/Regular Expressions/Actual_Data.txt")
# doc = fhandle.read()
# textNum = re.findall('[0-9]+', doc)
# for convert in textNum:
#     convert = float(convert)
#     numbers.append(convert)
# print(sum(numbers))

#Shorter Version
print(sum(float(num) for num in re.findall('[0-9]+',open("Python/Python - Access Web Data/Regular Expressions/Actual_Data.txt").read())))   