def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    min_ = 0
    max_ = len(A) - 1
    while min_ < max_:
        mid = (min_ + max_) // 2
        if A[mid] < A[mid+1]:
            min_ = mid+1
        else:
            max_ = mid
        print('mid:' , mid)
        print('min:' , min_)
        print('max:' , max_)
    return min_

def peakIndexInMountainArray2(A):
    """
    :type A: List[int]
    :rtype: int
    """
    maxx = A[0]
    i = 0
    while A[i] >= maxx:
        maxx = A[i]
        i += 1
    return i - 1


def peakIndexInMountainArray3(self, A):
    for i in xrange(len(A)):
        if A[i] > A[i+1]:
            return i

B = [0,1,0]
print(peakIndexInMountainArray(B))