def printPair(arr,arr_size,sum):
    s=set()
    for i in range(0,arr_size):
        temp=sum-arr[i]
        if(temp in s):
            print("Pair having the given sum:"+str(sum)+" is ("+ str(arr[i])+"," + str(temp) + ")")
        s.add(arr[i])

L=[0,12,5,4,6,9]
n=9
printPair(L,len(L),n)
