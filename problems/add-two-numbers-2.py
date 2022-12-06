# TODO: need to solve the problem using linked list.
def linked_list_sum(l1, l2):
    result = []

    max_list, min_list = l1, l2
    
    if len(l2) > len(l1):
        max_list, min_list = l2, l1
    rem = 0
    for i in range(len(max_list)):
        try:
            temp = str(max_list[i] + min_list[i] + int(rem))
        except:
            temp =  str(max_list[i] + int(rem))

        add = temp[0]
        if len(temp) == 2:
            rem = temp[0]
            add = temp[1]
        else:
            rem = 0
        result.append(int(add))
    if rem != 0:
        result.append(int(rem))
    return result



linked_list_sum([9,9,9,9,9,9,9], [9,9,9,9])
linked_list_sum([2,4,3], [5,6,4])
linked_list_sum([0], [0])
