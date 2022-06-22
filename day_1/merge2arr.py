# merge two sorted arrays

'''
Merge two sorted arrays without using any extra space
'''


def merge2Array(a,b):
    len_a = len(a)
    len_b = len(b)

    '''
    i=0
    j=0
    k=len_a-1

    while i<k and j<len_b:
        if a[i]<b[j]:
            i+=1
        else:
            temp = b[j]
            b[j]=a[k]
            a[k]=temp

            j+=1
            k-=1
        
    a.sort()
    b.sort()

    '''
    

    # one more way to sort

    for i in range(len_a):

        if a[i]>b[0]:
            temp = a[i]
            a[i]=b[0]
            b[0]=temp

            first = b[0]
            #now move b[0] to its correct position


            '''
            example -

            a1 =[1,3,5,7]
            b1 =[0,2,6,8,9]

            compare a[i] with b[0], if b[0]<a[i], swap 

            now sort array b so that a[i] at b[0] is sorted , after b is sorted , again perform the comparision of a[i] , with b[0] and repeat till we get the sorted array
            '''
            # here we are sorting array b so that it is at its correct position
            k=1

            while k<len_a and b[k]< first:
                b[k-1]=b[k]
                k+=1
            b[k-1]=first

if __name__ == '__main__':
    a=[1,3,5,7]
    b = [0,2,6,8,9]

    merge2Array(a,b)
    print(a)
    print(b)





