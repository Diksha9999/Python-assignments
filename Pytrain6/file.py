
files=open('f.txt','w')
string=input("enter details of a file")
files.write('hey diksha\n')
files.write("palash\n")
files.write(string)
files.close()


files=open('f.txt','r')
n=files.read()
print(n)
files.close()

files=open('f.txt','a')
string=input("enter new appending data")
files.write(string)
files.close()


'''

#opena file for reading data linewise
file1=open('phillos.txt','r')
line=file1.readline()
line1=file1.readline()
print(line)
print(line1)












'''