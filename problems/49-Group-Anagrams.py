from collections import defaultdict

def group_anagrams(strs) -> list:
    groups = defaultdict(list)
    for str in strs:
        print('here')
        count = [0]*26
        for char in str:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(str)
    return groups.values()


print(group_anagrams([""]))



