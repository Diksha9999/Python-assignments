a=input("enter Student's first Name: ")
i=[]
i.append(a)
for b in range(5):
    k=int(input("Enter theory marks:-"))
    i.append(k)
for c in range(3):
    k=int(input("Enter Practical marks:-"))
    i.append(k)
j=i[1:6]
jsum=sum(j)

k=i[6:9]
ksum=sum(k)



s=sum(j+k)
per=(s/500)*100
print("robert obtained",jsum, "marks out of 460 in theory and",ksum,"marks out of 40 in practical and successfully passed in exam with ",per,"in aggregate.Many congrats to Rober.")

