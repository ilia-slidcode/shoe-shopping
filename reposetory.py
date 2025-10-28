import data
import entities

def add (size: int, color: str,code: int):
    x=entities.shoe(size,color,code)
    data.shoes.append(x)
    
def remove (item):
    data.shoes.remove(item)
    
def show ():
    for item in data.shoes:
        print(item.size)
        print(item.color)
        print(item.code)
        print("-----------------------------")