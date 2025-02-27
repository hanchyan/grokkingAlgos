def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        # the line below is what makes it recursive. it calls quicksort again in the return
        return quicksort(less) + [pivot] + quicksort(greater) 
print quicksort ([10,5,2,3])   