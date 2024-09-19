#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Check for invalid characters
    for char in roman_string:
        if char not in data:
            return 0

    # Check for invalid repeated numerals (e.g., IIII, VV, etc.)
    if "IIII" in roman_string or "VV" in roman_string or "XXXX" in roman_string \
        or "LL" in roman_string or "CCCC" in roman_string or "DD" in roman_string \
        or "MMMM" in roman_string:
        return 0
    
    # Check for invalid subtractive combinations
    invalid_combinations = ["IL", "IC", "ID", "IM", "VX", "VL", "VC", "VD", "VM",
                            "XD", "XM", "LC", "LD", "LM", "DM"]
    for combination in invalid_combinations:
        if combination in roman_string:
            return 0
    
    numbers = [data[char] for char in roman_string]
    total = 0

    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            total -= numbers[i]
        else:
            total += numbers[i]

    return total + numbers[-1]

