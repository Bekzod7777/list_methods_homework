def main(fruits):
    bb=[]
    a=fruits.count('apple')
    bb.append(a)
    if a==1:
        bb.append(fruits.index('apple'))
    elif a==2:
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
    elif a==3:
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
    elif a==4:
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        
    elif a==5:
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
        bb.append(fruits.index('apple'))
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    return  bb
