def partition(elements,start,end): 
    pivot_index = start
    pivot = elements[pivot_index]
 

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1
                
        while elements[end] > pivot:
            end-=1

        if start < end:
            elements[start],elements[end] = elements[end],elements[start]

    elements[pivot_index],elements[end] = elements[end],elements[pivot_index]
    return end


def quick_sort(elements, start, end):
    if start< end:
        pi = (partition(elements, start,end))
        quick_sort(elements,pi+1,end)
        quick_sort(elements,start,pi-1)
        
    return elements



def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort_1(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        pi = partition_1(elements, start, end)
        quick_sort_1(elements, start, pi-1)
        quick_sort_1(elements, pi+1, end)

def partition_1(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index


if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
    
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    print(quick_sort(elements, 0, len(elements)-1))
    