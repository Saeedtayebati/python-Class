###Validation:
PATH="C:\Users\Mavara\Desktop\class\database.txt"

def validation():
    if not os.path.exists(PATH):
        f=open(PATH,"w+")
        f.write("")


def add(name,number):
    validation()
    f=open(PATH,"a+")
    new_phone=name + ":" + number + "\n"
    f.write(new_phone)
    f.close()


def search(name):
    validation()
    f=open(PATH,"r")
    for line in f.readlines():
        if name==line.split(":")[0]
            print(name + ":" + line.split(":")[1])
    f.close()

def delete(name):
    validation()
    f=open(PATH,"r")
    new_database=""
    for line in f.readlines():
        if not name==line.split(":")[0]
            new_database +=line
    f.close()
    f.open(PATH,"w")
    f.write(new_database)

def show_all():
    validation()
    f=open(PATH,"r")
    database=""
    database=f.read()
    f.close()
    print(database)



i=1
while i!=0:
    print("1-Add User\n2-Search Phone\n3-Delete Phone\n4-Show All Number\n0-Exit")
    i=int(input("Enter your choice:"))

    if i==1:
        name=input("Enter name:")
        number=input("Enter Number:")
        add(name,number)

    elif i==2:
        name=input("Enter name:")
        search(name)
    elif i==3:
        name=input("Enter name:")
        delete(name)
    elif i==4:
        show_all()
