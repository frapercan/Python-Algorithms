## https://www.hackerrank.com/challenges/diagonal-difference


def diagonalDifference(n, a, zero, acc1, acc2):
    if(n == 0):
        return abs(acc1-acc2)
    else:
        return diagonalDifference(n-1, a,zero+1, acc1 = acc1+ a[n-1][n-1],acc2 = acc2 + a[zero][n-1])
    
    
print(diagonalDifference(n,a,0,0,0))
        
    