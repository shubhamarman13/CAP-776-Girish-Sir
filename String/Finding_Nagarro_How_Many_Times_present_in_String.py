""" in this code we are having a string in  form which we are going to find
that how many times a nagaro word is present in the entire sentence """

sentence = "Nagarro is a great company. Many people at Nagarro believe that Nagarro provides excellent opportunities. Nagarro's culture is one of the best. If you work at Nagarro, you'll find Nagarro to be a fantastic place to grow."

count=0
sentence=sentence.lower()
print(sentence)
val=""
items=sentence.split(" ")
print(items)
value="nagarro"
for i in items:
    for j in i:
       val=val+j
       if val==value:
           print(val)
           count+=1
    val=""
print(count)




"""sentence = "Nagarro is a great company. Many people at Nagarro believe that Nagarro provides excellent opportunities. Nagarro's culture is one of the best. If you work at Nagarro, you'll find Nagarro to be a fantastic place to grow."
sentence=sentence.lower()
# Count the occurrences of the word "Nagarro"
count = sentence.count("nagarro")

print("The word 'Nagarro' appears", count, "times.")
"""
