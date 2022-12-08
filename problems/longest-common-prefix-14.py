def longest_common_prefix(strs):
    # sort the strings in ascending order by the length
    strs = sorted(strs, key=len)
    smallest_str = strs[0]
    com_prefix = ""
    for i in range(len(smallest_str)):
        for j in range(1,len(strs)):
            if smallest_str[i] != strs[j][i]:
                return com_prefix
        com_prefix += smallest_str[i]
        # print(com_prefix)
    return com_prefix 



# Solution using set and zip
def longest_common_prefix_zip(strs):
    com_prefix = ""
    for n in zip(*strs):
        if len(set(n)) == 1:
            result += n[0]
        else:
            return result
    return result


print(longest_common_prefix(["flower","flow","flight"]))