# fruit = "Banana"
# for sound in fruit:
#     print(sound)

# fruit = "banana"
# "bn" in fruit

text = "X-DSPAM-Confidence:    0.8475"
fpos = text.find("0")
lpos=len(text)
value = text[fpos : lpos]
print(float(value))
