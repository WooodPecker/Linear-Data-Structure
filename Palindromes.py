from DoubleQueen import DoubleQueen

def palindromestest(expression): # 回文检测
    dqueen = DoubleQueen()
    for string in expression:
        dqueen.addrear(string)
    ispalindromes = True
    while dqueen.size() > 1 and ispalindromes:
        first = dqueen.removerear()
        last = dqueen.removefront()
        if first != last:
            ispalindromes = False
    return ispalindromes


print(palindromestest("adkj;aldjf"))
print(palindromestest("radar"))
