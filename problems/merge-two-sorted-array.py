
def merge_two_sorted_list(l1, l2):
	
	# O(1)
	length = len(l1)  + len(l2)

	sorted_list = []
	i = 0
	j = 0

	while i < len(l1) and j < len(l2): 
		if l1[i] <= l2[j]:
			val = l1[i]
			i += 1
		else:
			val = l2[j]
			j += 1
		sorted_list.append(val)
	# sorted_list.extend(l1[i:] + l2[j:])
	while i < len(l1):
		sorted_list.append(l1[i])
		i += 1 
	while j < len(l2):
		sorted_list.append(l2[j])
		j += 1
	return sorted_list


l1 = [2, 5, 6, 7, 9, 9]
l2 = [-1, 0, 1, 1, 3]
print(merge_two_sorted_list(l1, l2))




