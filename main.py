import string 
from postfix import infixToPostfix 
from nfa import evaluate, search

def addConcatenationOperator(reg):
    """
    Explicitly add the '.' as concatenation operator so that we can process all operations 
    easily when using a stack to evaluate the expression(in construction of a nfa)
    """
    out = ''
    for i in range(len(reg)):
        token = reg[i]
        out += token
        if token in ['(', '|']:
            continue
        if (i < len(reg)- 1):
            lookAhead = reg[i+1]
            if lookAhead in ['*', '|', ')']:
                continue
            out += '.'
    return out

def tokenize(r):
    r = addConcatenationOperator(r)
    return [x for x in r]

def regex():
    # r = input('Enter your regex: ')
    r = '(a|b)*ab*a'
    assert all([x in ['(', ')','|', '.', '*'] or x in string.ascii_lowercase for x in r]), "invalid regex expression"
    # w = input('Enter word to try match against: ')
    w = 'abbaabbba'
    assert all([x in ['(', ')','|', '.', '*'] or x in string.ascii_lowercase for x in w]), "invalid word"

    infix_tokens = tokenize(r)
    postfix_tokens = infixToPostfix(infix_tokens)

    try:
        nfa = evaluate(postfix_tokens)
        if search(nfa, w):
            print("Match")
        else:
            print("No match")
    except Exception as e:
        print("Malformed regex:", str(e))


# ---- (abc)*(a)
if __name__=='__main__':
    regex()
    
