#""" emplement a python program that determine if all pranthesis in a given string from matching pairs """

def check_parenthese_balance(code_line):
    stack = []
    
    for char in code_line:
        if char == '(':
            stack.append(char)
            print(stack)
            
        elif char == ')':
            if not stack:
                return False
            print(stack)
            stack.pop()
            
    return len(stack) == 0
print(f"'(a+b)*c)':{check_parenthese_balance('((a+b)*c)')}")