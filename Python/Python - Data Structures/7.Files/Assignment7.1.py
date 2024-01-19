# Assignment 7.1
# Q. Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below. You can download the sample data at http://www.py4e.com/code3/words.txt

while True:
    fname = input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("Incorrect File Name:", fname)
for line in fhandle:
    line = line.rstrip()
    print(line.upper())   

# -------------------------------------------------------------------------------