def main(fruits):
    a=fruits.count('apple')
    if a==1:
        fruits.remove('apple')
    elif a==2:
        fruits.remove('apple')
        fruits.remove('apple')
    elif a==3:
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
    elif a==4:
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
        
    elif a==5:
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
        fruits.remove('apple')
    return fruits
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    
