def linear_index_search(number_list,number_to_find):
    for index,element in enumerate(number_list):
        if element == number_to_find:
         return index
    return -1   #this is the standard notation form where when you dont find a element then you return -1 which is a standard practise


def binary_search_index(number_list,number_to_find):
   left_index = 0
   right_index= (len(number_list) - 1 )
   middle_index = 0
    # now we use double slash to find the number the decimal otherwise if you use the single slash then you get the whole number with the decimal part
   while left_index <= right_index:
    middle_index = (left_index + right_index)//2
    if number_to_find == number_list[middle_index]:
        return middle_index
    
    if number_to_find < number_list[middle_index]:
        right_index = middle_index - 1
    else:
       left_index = middle_index + 1

    return -1
   
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def binary_search_all(arr, target):
    def binary_search_left(arr, target):
        low, high = 0, len(arr) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid  # record the index
                high = mid - 1  # keep searching in the left half
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index

    def binary_search_right(arr, target):
        low, high = 0, len(arr) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid  # record the index
                low = mid + 1  # keep searching in the right half
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index

    left_index = binary_search_left(arr, target)
    right_index = binary_search_right(arr, target)

    if left_index == -1:
        return []  # Target not found

    return list(range(left_index, right_index + 1))


# Test
arr = [1, 1, 2, 2, 2, 4, 5]
target = 2
indices = binary_search_all(arr, target)
print(indices)

      
      

#    right_index = index + 1

# if __name__ == '__main__':
#     numbers_list = numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#     number_to_find = 15  
#     print(len(numbers_list))

#     index = recursive_binary_search(numbers_list, number_to_find, 0, len(numbers_list))
#     print(f"Number found at index {index} using binary search")