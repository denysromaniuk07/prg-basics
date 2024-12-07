import queue
###3.3 

# expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
# expression2 = "[(2+3]/4)"                 # brackets not correct
# expression3 = "(2-3*4+(5/6)"              # brackets not correct

# def brackets_ok(expression):
#     stack  = queue.LifoQueue()
#     for char in expression:
#         if char not in '(){}[]':
#             continue
        
#         if char in '([{':
#             stack.put(char)
        
#         elif char in ')]}':
#             if stack.empty():
#                 return False
#             top = stack.get()
#             if (top == '(' and char!= ')') or (top == '[' and char!= ']') or (top == '{' and char!= '}'):
#                 return False
#     return stack.empty()


# if brackets_ok(expression1):
#    print("OK")
# else:
#    print("NOT OK")

# if brackets_ok(expression2):
#     print("OK")
# else: 
#     print("NOT OK")

# if brackets_ok(expression3):
#     print("OK")
# else:
#     print("NOT OK")

###3.4

def decimal_to_binary(n):
    stack = queue.LifoQueue() # create a stack

    while n > 0:  
        remainder = n % 2 
        stack.put(remainder)
        n = n // 2
    
    binary = ""
    while not stack.empty():
        binary += str(stack.get())
    
    return binary

n = 18



print(f"Natural number: {n}")
print("Binary number: ", decimal_to_binary(n))