from pathlib import Path
import os
def fileover():
     path=Path('')
     items=list(path.rglob('*'))
     for i ,items in enumerate(items):
          print(f"{i+1} : {items}")

def createfile():
    fileover()
    try:
        name = input("enter the path for the new file: ")
        p=Path(name)
        if not p.exists():
            with open(p,'w') as f:
                data=input("enter the data to write in the file : ")
                f.write(data)
        else:
            print("file already exists ")
    except Exception as e:
        print("an error occured as : ", e)

def updatefile():
    fileover()
    name =input("which file do you want to update : ")
    p=Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changong the file name ")
        print("press 2 for overwriting")
        print("press 3 for appending the data")
        res =int(input(" Enter Your Response: " ))
        if res==1:
            name2=input("enter the new file name :")
            p2=Path(name2)
            p.rename(p2)
        elif res ==2:
            with open(p,'w') as f:
                data=input("enter what you want to over write")
                f.write(data)
    else:
        print("file doesnt exist : ")


    


def readfile():
    
        name=input("enter the file name for read : ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as f:
                data=f.read()
                print(data)
                print("file readed succesfully")
        else:
            print("file does not exist")
        
            
    
def deletefile():
    fileover()
    try:
        name = input("enter the file name for delete : ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file deleted successfully")
        else:
            print("file does not exist")
    except Exception as e:
        print("an error occured as : ", e)



print("choose 1 for create file")
print("choose 2 for read file")
print("choose 3 for delete file")
print("choose 4 for update file")
option=input("enter the option : ")


if option == "1":
    createfile()

elif option == "2":
    readfile()
elif option == "3":
    deletefile()
elif option == "4":
    updatefile()

print("thank you for using this program ")
