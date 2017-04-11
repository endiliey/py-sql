def anagram(s1, s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    if len(s1) != len(s2):
        return False
    count = {}
    
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s2:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
        else:
            return False
        
    return True

print(anagram('endi', 'idne'))
print(anagram('endi', 'IDNE'))
print(anagram('endo', 'inde'))
