myList=[""]
def delete():
    deleteKey=int(input("Enter the Task's Number to Delete:"))
    for i in range(1,len(myList)):
        if i==deleteKey:
            myList.pop(i)
            print("Element Remove Successfully")
            break
        else:
            print("Element Not Found")
def display():
    print("***********************************")
    for i in range(1,len(myList)):
        print(i,end=" ")
        print(myList[i])
    print("***********************************")
def  create():
    element=input("Enter Element :")
    myList.append(element.upper())
def update():
    checkKey=int(input("Enter the Task's Number to Update:"))
    changeValue=input("Enter The New Value : ")
    for i in range(1,len(myList)):
        if i==checkKey:
            myList[i]=changeValue
            break
        else:
            print("Element Not Found")

while True:
    print("1. For Adding items in the List.")
    print("2. To Display the Items in the List.")
    print("3. Update an item from the List.")
    print("4. Delete an Item from the List.")
    choice=int(input("Enter Your Choice:"))
    if(choice<1 or choice>4):
        print("Invalid Input Please Enter Again!")
    if (choice==1):
        create()
    if(choice==2):
        display()
    if(choice==3):
        update()
    if(choice==4):
        delete()
   
    print("\nDo You Want to Continue, Press y to Continue.")
    ch=str(input())
    if(ch!='y'):
        break
    
