import re
str="English=78 Science=83 MAth=68 History=65"
marks=[int(n) for n in re.findall(r'\b\d+\b',str)]
totlmarks=0
for mark in marks:
    totlmarks+=mark
per=totlmarks/len(marks)
print("Total marks :",totlmarks,"percentage :",per)