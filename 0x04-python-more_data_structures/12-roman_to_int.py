#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        z = len(roman_string) - 1
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(z + 1):
            for rletter in num:
                if roman_string[i] == rletter:
                    if i == z and roman_string[z - 1] < roman_string[z]:
                        result += num[rletter] - 2
                    else:
                        result += num[rletter]
                    break
        return result
