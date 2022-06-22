# subarray with a given sum

'''
given an unsorted array A of size N , contains non-ve integers, find continuous sub-array
'''

def subarraySum(A,S):
    N = len(A)

    #brute force
    '''
    ------------------------------------------------
    for i in range(N):
        sumVal=0
        for j in range(i,N):
            sumVal+=A[j]
            if sumVal == S:
                print(i,j) #this will give the index as index starts from 0 , if we require position then postion starts from 1 , so add 1 to both i,j
                return
    -------------------------------------------      
    '''

    #optimum method - 
    '''
    using hashing

    d ={} #hashmap
    sum_so_far = 0

    for i in range(N):
        sum_so_far+=A[i]
        
        #now check if there exist one sublist with the given sum

        if sum_so_far==S:
            return ((0,i))

        if(sum_so_far-S) in d:
            return(d[sum_so_far-S]+1,i)

        d[sum_so_far]=i

    return -1


    '''

    # ------------------------------------------

    # one more approach we can take here by using two pointers

    currsum = A[0]
    start=0
    i=1
    while i<=N:
        #if current sum exceeds the sum and start < i-1
        while currsum>S and start<i-1:
            currsum-=A[start]
            start+=1

        if currsum == S:
            return(start,i-1)

        if i<N:
            currsum+=A[i]
        i+=1

    return -1



    
if __name__ =='__main__':
    A = [10, 2, -2, -20, 10]
    S=0
    print(subarraySum(A,S))
    