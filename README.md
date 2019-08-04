# Transfer
def binary(list1, item):
    first=0
    last=len(list1)-1
    found=False
    while first<=len(list1) and not found:
        midpoint=(first+last)//2
        if list1[midpoint]==item:
            found=True
        else:
            if item<list1[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
l=[1,2,3,4,233]
print(binary(l,3))
print(binary(l,5))

def binaryrecursion(list1, item):
    if len(list1)==0:
        return False
    else:
        midpoint=len(list1)//2
        if list1[midpoint]==item:
            return True
        else:
            if list1[midpoint]<item:
                return binaryrecursion(list1[midpoint+1:],item)
            else:
                return binaryrecursion(list1[:midpoint-1],item)
print(binaryrecursion(l,3))
print(binaryrecursion(l,5))
