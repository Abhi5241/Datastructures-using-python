stack=[]
def push():
    if len(stack)==n:
        print("stack is full")
    else:
        element=input("Enter the element:\n")
        stack.append(element)
        print(stack)
def pop_element():
    if  stack==[]:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)

n=int(input("enter the limit of stack:"))    
while True:
    print("select the operation 1. push  2. pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif(choice==2):
        pop_element()
    elif(choice==3):
        break
    else:
        print("please enter the correct choice")
    






