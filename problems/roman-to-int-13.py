# convert roman number to equivalent integer number
def roman_to_int(s):
    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    index = len(s) - 1
    int_num = 0
    while index >= 0:
        right_val = symbol[s[index]]
        left_val = symbol[s[index - 1]]
        # print(f'index: {index} left:({s[index]}) {left_val} right:({s[index-1]}) {right_val}')
        parse_val = right_val
        if left_val < right_val and index != 0:
            parse_val = right_val - left_val
            index -= 1
        # print(f'parse_val: {parse_val}')
        int_num += parse_val
        # print(f'Total: {int_num}')
        index -= 1
    return int_num
    
print(roman_to_int('MCMXCIV'))


