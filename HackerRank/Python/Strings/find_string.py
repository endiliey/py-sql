def count_substring(string, sub_string):
    sum = 0
    st = string.find(sub_string, 0)
    l = len(sub_string)
    while (st != -1):
        sum += 1
        st = string.find(sub_string, st + l - 1)
    return sum
        