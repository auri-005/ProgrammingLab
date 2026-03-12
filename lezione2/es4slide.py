def check_list(A, B):
    for elem in A:
        if elem in B:
            return True
    return False

list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11]
check_list(list1, list2)
