from re import S
from this import s


def main(list1):
    s=[]
    bir=list1.count(1)
    nol=list1.count(0)
    s.append(bir)
    s.append(nol)
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    return s
list1=[1,0,1,0,0,0,0,1]
print(main(list1))
    