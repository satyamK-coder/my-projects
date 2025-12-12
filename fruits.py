
def addfruit(fruits,item):
    fruits.append(item)
    return(fruits)



def checkfruits(fruits,item):
    if item in fruits:
        return True
    else : 
        return False

def getindex(fruits,item):
    count=0 
    for fruit in fruits:
        if item == fruit:
            return(count)
        else:
            count=count+1