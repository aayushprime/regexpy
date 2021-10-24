# regexpy
Simple Regex Engine implemented in python (supports union, concatenation and Kleene star only)
# How it works (Overview)
- Input infix regex is converted into postfix expression
- Postfix expression is evaluated to construct a NFA(Thompson's construction)
- Constructed NFA is searched using ε-closure

# Syntax
- Union (`\`)
- Kleene Star (`*`)
- Concatenation (Blank)

Escape Sequences not supported yet. The letters of the language are lowercase ASCII letters.
