a=int(input("Enter a 5 digit number:"))
sum=0
while(a!=0):
    sum=sum+int(a%10)
    a=int(a/10)
print(sum)