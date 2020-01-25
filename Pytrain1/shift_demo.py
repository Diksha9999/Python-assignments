a=int(input())
ls=a<<1
mul_2=a*2
if(ls==mul_2):
    print("yes it can be used to multiply by 2(left shift) ",ls)
else:
    print("no it cant be used to multiply 2 ",mul_2)
rs=int(a>>1)
div_2=int(a/2)
if(rs==div_2):
    print("yes it can be used to divide by 2(right shift) ",rs)
else:
    print("no it cant be used to divide 2 ",div_2)