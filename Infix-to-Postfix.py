OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} 

def count(expression):
    count = 0
    for char in expression:
        if char.isalpha():
            count += 1
    return count

def infix_to_postfix(expression):
    myStack = []  
    output = ''   
    for ch in expression:
        if ch not in OPERATORS:
            output += ch           
        elif ch == '(': 
            myStack.append('(')     
        elif ch == ')':                      
            while myStack and myStack[-1] != '(':
                output += myStack.pop()
            myStack.pop()
        else: 
            while myStack and myStack[-1] != '(' and PRIORITY[ch] <= PRIORITY[myStack[-1]]:
                output += myStack.pop()
            myStack.append(ch)
    while myStack:      
        output += myStack.pop()
    return output 

def isFull():
    global top, max
    if top == max - 1:
        return True
    return False

def doPush(a):
    global top, s, max
    if not isFull():
        top +=1
        s[top] = a
    else:
        print("the stack is Full")

def isEmpty():
    global top
    if top == -1:
        return True
    return False

def dopop():
    global top, s
    if not isEmpty():
        a = s[top]
        top -= 1
        return a
    return -1

def evalpostfix(Enter_postfix):
    global top
    for ch in Enter_postfix:
        if ch in ["+", "-", "*", "/"]:
            r = dopop()
            l = dopop()
            if ch == "+":
                x = l + r
                doPush(x)
            elif ch == "-":
                x = l - r
                doPush(x)
            elif ch == "*":
                x = l * r
                doPush(x)
            elif ch == "/":
                x = l / r
                doPush(x)
        else:
            x = int(input("Enter the value : "))
            doPush(x)
    return dopop()
def reset_variables():
    global top, s, max
    top = -1
    s = [None] * max
while True:
    expression = input('Input Expression :')
    postfix_expression = infix_to_postfix(expression)
    max = count(expression)
    s = [None] * max
    top = -1
    res = evalpostfix(postfix_expression)
    print("The Result is: ", res)
    reset_variables()