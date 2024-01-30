# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fhandle = open("Python/Python - Data Structures/10.Tuples/mbox-short.txt")
hours = list()
freq = dict()
for line in fhandle:
    if line.startswith('From') and not line.startswith('From:'):
        hours.append(line.split()[5].split(':')[0])
for hour in hours:
    freq[hour] = freq.get(hour,0) + 1
for key,value in sorted(freq.items()):
    print(key, value)