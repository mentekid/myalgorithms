def naive(text, key):
    positions = []
    nBig = len(text)
    nSmall = len(key)
    if nBig < nSmall:
        return positions

    for i in range(nBig-nSmall+2):
        found = True #found at this position
        check=i
        for j in range(nSmall):
            if text[check] != key[j]:
                found = False
                break
            else:
                check+=1
                continue
        if found:
            positions.append(i)
    return positions


text = "1234545345"
key = "345"

print naive(text, key)
