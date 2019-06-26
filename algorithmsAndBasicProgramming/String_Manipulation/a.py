from collections import Counter
def isValid(s):
    # Complete this function
    s1 = Counter(s)
    print(s1)
    values = list(s1.values())
    val_max = max(values)
    val_min = min(values)
    print(values.count(val_max))
    #  all frequencies are same  or remove one max-frequency or remove one min-frequency
    if val_max == val_min or (val_max - val_min == 1 and values.count(val_max) == 1) or (val_min == 1 and values.count(val_min) == 1):
        return 'YES'
    else:
        return 'NO'

print(isValid('aabbc'))