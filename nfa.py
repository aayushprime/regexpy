# A object representing a state in the NFA
class State:
    def __init__(self):
        self.ETransitions = []
        self.Transitions = {}

    def addETransition(self, other):
        self.ETransitions.append(other)
    
    def addTransition(self, other, letter):
        self.Transitions[letter]= other

"""
Hidden Details

A NFA is a tuple of 2 states
NFA = (state1, state2)
state1 is the start state
state2 is the end state
(only 1 end state in Thompson's construction)


"""



# methods of evaluation(combining smaller NFAs into bigger NFA)
# operations are either Union, Concatenation, Kleene Star
def union(nfa1, nfa2):
    start = State()
    end = State()
    start.addETransition(nfa1[0])
    
    start.addETransition(nfa2[0])
    
    nfa1[1].addETransition(end)
    nfa2[1].addETransition(end)

    return (start,end)

def concatenation(nfa1, nfa2):
    nfa1[1].addETransition(nfa2[0])
    return (nfa1[0], nfa2[1])

def kleeneStar(nfa):
    start = State()
    end = State()

    start.addETransition(end)
    start.addETransition(nfa[0])
    nfa[1].addETransition(nfa[0])
    nfa[1].addETransition(end)

    return (start, end)

# Simple NFAs created from scratch to bootstrap the NFA creation(base case)
def simpleE():
    start = State()
    end = State()
    start.addETransition(end)
    return (start, end)

def singleLetter(token):
    start = State()
    end = State()
    start.addTransition(end, token)
    return (start, end)

# convert postfix_expression to nfa
def evaluate(postfix_expression):
    stack = [] if len(postfix_expression) != 0 else [simpleE()]
    for token in postfix_expression:
        if token not in ['*', '.', '|']:
            stack.append(singleLetter(token))
        else:
            if token == '*':
                operand1 = stack.pop()
                stack.append(kleeneStar(operand1))
            elif token == '.':
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(concatenation(operand1, operand2))
            elif token == '|':
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(union(operand1, operand2))
    
    return stack[0]

# find the EClosure of a state, visited parameter is for bookkeeping only
def EClosure(state, visited):
    output = [state]
    for NextState in state.ETransitions:
        if NextState not in visited:
            output+=EClosure(NextState, visited)
            visited.append(NextState)
    return output

# given a nfa and a word search the nfa to find out whether the word is a match
def search(nfa, word):
    # starting states are the EClosure of the start state
    currentStates = EClosure(nfa[0], [])

    for letter in word:
        nextStates = []
        for state in currentStates:
            if letter in state.Transitions:
                nextStates += EClosure(state.Transitions[letter], [])
        currentStates = nextStates

    # if final state of NFA(end) is reached at the end
    return nfa[1] in currentStates
