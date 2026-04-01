import matplotlib.pyplot as plt
def insertionsort(array):
    n=len(array)
    for i in range(0,n):
        item=array[i]
        j=i-1
        while i>0 and item <array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=item
    return array
array=[]
n=int(input("how many elements you want in your array"))
for i in range(n):
    array.append(int(input("enter %d:" elements %i)))
print(f"before swaping:(array)")
array=insertionsort(array)
print(f"after swapping:(array)")
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Time complexity of insertionsort is o(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
