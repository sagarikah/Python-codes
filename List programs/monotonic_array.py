##    Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
##    An array is monotonic if it is either monotone increasing or monotone decreasing.
##    An array A is monotone increasing if for all i <= j, A[i] <= A[j].
##    An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
##    Return “True” if the given array A is monotonic else return “False”
##
##    Examples:
##
##    Input : 6 5 4 4
##    Output : true
##
##    Input : 5 15 20 10
##    Output : false




A = list(map(int, input().split()))
n = len(A)


def is_monotone_increasing(A,n):
    flag = 0
    
    for i in range(0,n-1):
        j = i+1
        if (A[i] > A[j]):
            flag = 1

    if (flag == 0):
        return 'True'
    else:
        return 'False'


def is_monotone_decreasing(A,n):
    flag = 0
    
    for i in range(0,n-1):
        j = i+1
        if (A[i] < A[j]):
            flag = 1

    if (flag == 0):
        return 'True'
    else:
        return 'False'



if A[0] < A[n-1]:
    res = is_monotone_increasing(A,n)
    print(res)

else:
    res = is_monotone_decreasing(A,n)
    print(res)
