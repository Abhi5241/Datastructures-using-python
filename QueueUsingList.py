queue=[]
def enqueue():
    element = input("Enter the element:\n")
    queue.append(element)
    print(element,"is added to queue!")

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e=queue.pop(0)
        print("Removed element:",e)
def display():
    print(queue)


while True:
    print("select the operation")
    print("1.Add \n2.Remove \n3.Show \n4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct choice")

