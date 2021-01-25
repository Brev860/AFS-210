list = [1,62,38,4,45,6,7]

# def listValue(a):
#     newlist = []
#     minChar = a[1]
#     length = len(a)
#     counter = 0
#     for i in a:
#         i = int(i)
#         if i <  minChar:
#              minChar = i
#              newlist.append(i)
#              a.remove(i)
#              counter = counter + 1
#              if counter == length:
#                 return newlist
    
    

            
    
# print(listValue(list))


a = [3, 1, 5, 2, 4]

def sortList(a):
    for i in a[1:]:
        j = a.index(i)
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1
    return j

print(sortList(a))

