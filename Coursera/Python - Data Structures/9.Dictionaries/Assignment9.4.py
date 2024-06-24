# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fhandle = open('Python/Python - Data Structures/9.Dictionaries/mbox-short.txt')
count = 0
mails = list()
maildix = dict()
for line in fhandle:
    line = line.strip()
    if line.startswith("From"):
        if not line.startswith("From:"):
            line = line.split()
            line = line[1]
            mails.append(line)
            count = count + 1
for id in mails:
    maildix[id] = maildix.get(id,0) + 1
bigCount = None
bigWord = None
for key,value in maildix.items():
    if bigCount is None or value > bigCount:
        bigCount = value
        bigWord = key
print(bigWord, bigCount)
 