# triplet count - Given an array of distinct integers , the task if to count all the triplets such that sum of two ele is equal to third



def tripletCount(A):
    count =0
    N=len(A)
    # brute force approach
    '''
    run three loops and see if the triplet exists or not

    '''


    # efficient approach 

    A.sort()

    i=N-1
    
    while i>0:
        j=0
        k=i-1

        while j<k:
            if A[i]==A[j]+A[k]:
                # print( 'Triplet exist' )
                j+=1
                k-=1
                count+=1

            elif A[i]>A[j]+A[k]:
                j+=1
            else:
                k-=1
        i-=1
    return count
    



if __name__ == '__main__':
    A = [1, 5, 3, 2]
    print(tripletCount(A))

        







