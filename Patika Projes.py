
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []

def flatten(a):
    for i in a:
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)
flatten(l)
print(l1)

#Proje-2

l2 = [[1, 2], [3, 4], [5, 6, 7]]
def reversed(l):
    l.reverse()
    
    for i in l:
        if type(i)==list:
            reversed(i)
            
reversed(l2)            
print(l2)







