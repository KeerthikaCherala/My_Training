def subsequences(s):
    if len(s) == 0:
        return ['']
    else:
        first_char = s[0]
        rest_str = s[1:]
        rest_subseq = subsequences(rest_str)
        return rest_subseq + [first_char + sub for sub in rest_subseq]
s=input()
print(subsequences(s))