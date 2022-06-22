# missing number - 
def missingNum(A):
    n=len(A)

    '''
    N = A[n-1]


    sum1 = sum(A)

    sum2 = (N*(N+1))//2

    return sum2-sum1
    
    '''
    
    # the above solution can cause overflow , so in order to avoid that we follow the below approach
    i,total = 0,1

    for i in range(2,n+2):
        total+=i
        total -=A[i-2]

    return total




print(missingNum([0,1,2,3]))