import data
import reposetory
import entities
import validation

while True:
    print("1: add ")
    print("2: remove ")
    print("3: show ")
    print("4: exit ")
    operation=input("what would you like to do ? ")
    
    if operation=="1":
        shoe=input("what shoe ?")
        size=input("the size? ")
        color=input("the color? ")
        code=input("the code? ")
        addvlad=validation.addver(shoe)
        if addvlad==False:
            continue
        else:
            reposetory.add(int(size), str(color), int(code))
            
    elif operation=="2":
        shoe=input("what shoe ?")
        size=input("the size ?")
        y=input("the color ?")
        z =input("the code ?")
        removevlad=validation.removever(shoe)
        if removevlad==False:
            continue
        else:
            reposetory.remove(shoe)
            
    elif operation=="3":
        reposetory.show()
        
    else:
        exit()