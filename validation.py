import data



def addver (shoe):
    if shoe in data.shoes:
        print("this item already exists in shoes")
        return False
    else:
        print("item was added to shoes ")
        return True
    
    
def removever (shoe):
    if shoe not in data.shoes:
        print("this item does not exist in shoes ")
        return False
    else:
        print("item was removed from shoes ")
        return True