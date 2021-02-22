
def search(arrs, x): 

    arrsize = int(len(arrs) - 1) 

    firstindex = 0 
    lastindex = arrsize 

    while firstindex <= lastindex: 
        mid = int((firstindex + lastindex)/2)

        if arrs[mid] == x: 
            return True 
        

        if x > arrs[mid]: 
            firstindex = mid + 1 
        else: 
            lastindex = mid - 1

        
    if firstindex > lastindex: 
        return False

a = [4,8,10,17,23,45,77]
print(search(a, 72))