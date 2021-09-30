### here we are defining the insertion sorting function and expecting the time complexity accordingly.
### Author: Himesh
def insertion_sort(A):
    k=len(A)                       #getting the length 
    for i in range(k):
        temp=A[i]					#assigning a temporary variable
        j=i-1
        while(j>=0 and A[j]>temp):         #sorting the elements until the insertion place is found
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp							# inserting our element and repeating the process to sort all the elements
    return A    
