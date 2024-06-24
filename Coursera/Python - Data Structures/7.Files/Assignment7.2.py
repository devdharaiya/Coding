# Assignment 7.2
# Q. Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

count = 0
array = 0.00

while True:
    fname = input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("Incorrect File Name:", fname)

for line in fhandle:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        fpos = line.find("0")
        lpos = len(line)
        values = line[fpos : lpos]
        number = float(values)
        array = number + array
print("Average spam confidence:", array/count)

# -------------------------------------------------------------------------------