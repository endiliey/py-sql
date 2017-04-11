if __name__ == '__main__':
    s = input()
    an, ab, digits, lc, uc = False, False, False, False, False
    for char in s:
        if char.isalnum():
            an = True
        if char.isalpha():
            ab = True
        if char.isdigit():
            digits = True
        if char.islower():
            lc = True
        if char.isupper():
            uc = True
    print(an)
    print(ab)
    print(digits)
    print(lc)
    print(uc)
