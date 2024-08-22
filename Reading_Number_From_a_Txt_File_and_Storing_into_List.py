"""Reading the inetegr from a file and then assigning them into a list by using
the split method and in the end appy some  functions like max mean median and so
on """

f = open("D:\\LPU\\SEM 3\\Python\\CAP-776-Girish-Sir\\file1.txt", 'r')
List1=[]
for lines in f:
    word=lines.split()
    for num in word:
        num=int(num)
        List1.append(num)
print(max(List1))
