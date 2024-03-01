"""მოცემულია რიცხვების სია `[94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]`
გამოიყენეთ სორტირების ალორითმები: `bubble sort`, `merge sort` და `insertion sort`.
შედეგები დაბეჭდეთ ეკრანზე."""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] , arr[j]



def merge_sort(arr):
    n = len(arr)
    middle = n // 2

    if n <= 1:
        return arr
    
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge_list(left, right)

def merge_list(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:] + right[j:]
    return result



def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        j = i

        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1 



arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

bubble_sort(arr)
print (f"Bubble Sort: {arr}")

print (f"Merge Sort: {merge_sort(arr)}")

insertion_sort(arr)
print (f"Insertion Sort: {arr}")