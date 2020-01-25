square1=[[4,9,2],[3,5,7,],[8,1,6]]
square=[[0,0,0,],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
		square[i][j]=int(input("Enter the value of square[{0}][{1}]: ".format(i,j)))
n=len(square)
dig1sum=dig2sum=0
for i in range(3):
	dig1sum=dig1sum+square[i][i]
	dig2sum=dig2sum+square[i][n-i-1]
for i in range(0,3):
 colsum=rowsum=0
 for j in range(0,3):
  colsum=colsum+square[j][i]
  rowsum=rowsum+square[i][j]
  if(colsum!=rowsum!=dig1sum!=dig2sum):
    print("No given square is not a Lo_Shu_Magic_Square")
    exit()

print("yes given square is a Lo_Shu_Magic_Square")