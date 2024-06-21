def can_form_string(num_strings, strings, target_string):
    char_count = {}
    for string in strings:
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for char in target_string:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return "no"
        else:
            return "no"

    return "yes"


num_strings = int(input())
strings = [input() for _ in range(num_strings)]
target_string = input()

print(can_form_string(num_strings, strings, target_string))