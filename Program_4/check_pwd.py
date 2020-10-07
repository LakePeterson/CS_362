def check_pwd(password):
    countUpper = 0
    countLower = 0
    countDigit = 0
    countSymbol = 0
    symbols = '~`!@#$%^&*()_+-='

    if len(password) < 8 or len(password) > 20:
        return False
    for i in password:
        if i.isupper():
            countUpper += 1
    if countUpper == 0:
        return False
    for i in password:
        if i.islower():
            countLower += 1
    if countLower == 0:
        return False
    for i in password:
        if i.isdigit():
            countDigit += 1
    if countDigit == 0:
        return False
    for i in password:
        for j in symbols:
            if i == j:
                countSymbol += 1
    if countSymbol == 0:
        return False
    return True
