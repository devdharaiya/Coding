# # Assignment 7.1
# while True:
#     fname = input("Enter File Name:")
#     try:
#         fhandle = open(fname)
#         break
#     except:
#         print("Incorrect File Name:", fname)
# for line in fhandle:
#     line = line.rstrip()
#     print(line.upper())   

# -------------------------------------------------------------------------------
# # Assignment 7.2
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