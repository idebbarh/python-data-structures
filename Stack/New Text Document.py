from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(string) :
    stack = Stack()
    rever_str = ""
    for c in string:
        stack.push(c)
    while not stack.is_empty() :
        rever_str+=stack.pop()
    return rever_str
print(reverse_string("We will conquere COVID-19"))

#Exercice 2 :
def is_match(close,open):
    match_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    return match_dict[close] == open

def is_balanced(string):
    stack = Stack()
    for c in string :
        if c in ["(","[","{"] :
            stack.push(c)
        if c in [")","]","}"] :
            if stack.is_empty() :
                return False
            if not is_match(c,stack.pop()) :
                return False
    return stack.size() == 0 
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))