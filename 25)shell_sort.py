def shellsort(element):
    size=len(element)
    gap = size //2

    while gap > 0:
        for i in range(gap,size):
            j = i
            anchor = element[gap] 
            while j>=gap and anchor < element[j-gap]:
                element[j] = element[j-gap]
                j-= gap
            element[j] = anchor
        gap = gap //2


