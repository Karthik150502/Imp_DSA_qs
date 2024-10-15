def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif token == "-":
            stack.append(-int(stack.pop()) + int(stack.pop()))
        elif token == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif token == "/":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(int(b / a))
        else:
            stack.append(token)
    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

'''
10, 6, 9, 3
10, 6, 12
10, 6, 12, -11
10, 6, -132
10, -792
-782

'''
res = evalRPN(tokens)
print(res)


