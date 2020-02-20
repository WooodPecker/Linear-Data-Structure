from Stack import Stack

def infixtopostfix(infixexrepssio):   # 将中缀运算 转换为 后缀运算
    prilev = {"/": 3, "*": 3, "-": 2, "+": 2,"(": 1}
    newstack = Stack()
    postfixList = []
    tokenlist = infixexrepssio.split()   # 将字符串拆分

    for token in tokenlist:
        # 运算主题：
        # 当为字符时则直接输出到列表
        # 当为左括号时压进 队列
        # 当为右括号时，队列最后的出栈进列表 直到 队列出栈的为 左括号
        # 当为运算符时， 和队列中的优先级对比，将优先级大于等于当前字符的运算符放进列表 并最后压入当前运算符

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)

        elif token == "(":
            newstack.push(token)

        elif token == ")":
            topToken = newstack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = newstack.pop()

        else:
            while ( not newstack.isEmpty() ) and ( prilev[newstack.peek()] >=  prilev[token] ):
                postfixList.append( newstack.pop() )
            newstack.push(token)

    # 将栈中剩余的运算符放进队列
    while not newstack.isEmpty():
        postfixList.append(newstack.pop())

    # 形成字符串
    return "".join(postfixList)

def caculation(exression): # 对后缀字符串进行运算
    savelist = Stack()
    ntokenlist = []
    for i in exression:
        ntokenlist.append(i)

    for token in ntokenlist:
        # 对于字符串的放进栈
        # 当为运算符时出栈两个数，第一个在运算符右边 第二个在运算符左边
        if token in "0123456789":
            savelist.push(token)
        else:
            num2 = savelist.pop()
            num1 = savelist.pop()
            result  = math(token,float(num1),float(num2))
            savelist.push(result)

    return savelist.pop()


def math(op,num1,num2):
    if op == "*":
        return num1 * num2

    elif op == "/":
        return  num1 / num2

    elif op == "+":
        return  num1 + num2

    else:
        return  num1 - num2



expresson = "1 * ( 3 + 4 ) * 5"
aftertrasform = infixtopostfix(expresson)
result = caculation(aftertrasform)
print(result)




