
def bubble_sort(a_list):
    # loop that allows you to go through all the elements of the list
    for i in range(0,len(a_list)):
        # cycle that allows to compare each element of the list
        for j in range(0,len(a_list)-i-1):
            # compare two adjacent elements
            if a_list[j] > a_list[j+1]:
                aux = a_list[j]
                # swapping elements if elements
                # are not in the intended order
                a_list[j] = a_list[j+1]
                a_list[j+1] = aux
    return a_list

unordered_list = [5,7,9,11,15,1,8]
print("unordered list: ",unordered_list)
ordered_list = bubble_sort(unordered_list)
print("ordered list: ", ordered_list)
