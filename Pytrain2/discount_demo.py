Qt=int(input("No. of packages purchased"))
if Qt in range(10,20):
    dsct=0.1
elif Qt in range(20,50):
    dsct=0.2
elif Qt in range(50,100):
    dsct=0.3
else:
    dsct=0.4
n=(Qt*99)*dsct
result=(Qt*99)-n
print("Amt discounted:",result)



