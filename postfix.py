import string

# defining the precedence of operators while conversion 
def precedence(operator_token):
    if operator_token in ['*']:
        return 4
    elif operator_token in ['.']:
        return 3
    elif operator_token in ['|']:
        return 2
    # important: precedence value of brackets is lower than all
    elif operator_token in ['(', ')']:
        return -1
    else:
        raise ValueError("The given token is not an operator")


# conversion algorithm using the stack
def infixToPostfix(infix_tokens):
    stack = []
    out = []
    for token in infix_tokens:
        # token is an operand
        if token in string.ascii_lowercase:
            out.append(token)
        elif token == '(':
            stack.append('(')
        elif token == ')':
            while stack[-1] != '(':
                out += stack.pop()
            stack.pop()
        else:
            # operator is scanned
            while len(stack) != 0 and precedence(token) <= precedence(stack[-1]):
                out += stack.pop()
            stack.append(token)
    while len(stack)!=0:
        out += stack.pop()
    return out   